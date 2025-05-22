import os
import subprocess
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, BackgroundTasks
from app.schemas.video import NestedVideoRead, VideoRead
from sqlalchemy.orm import Session, joinedload
from datetime import datetime
from app.database import get_db
from app.models import AthleteVideoTag, Video
import time
from fastapi.responses import FileResponse

router = APIRouter(prefix="/videos", tags=["Videos"])

UPLOAD_DIR = "./video_files"

@router.post("/upload")
def upload_video(background_tasks: BackgroundTasks, file: UploadFile = File(...), db: Session = Depends(get_db)):

    if file.content_type not in ["video/mp4", "video/quicktime"]:
        raise HTTPException(status_code=400, detail="Only mp4 and mov files allowed")
    
    existing = db.query(Video).filter_by(filename=file.filename).first()
    if existing:
        raise HTTPException(status_code=400, detail="A video with this filename already exists")

    file_location = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_location, "wb") as buffer:
        buffer.write(file.file.read())

    duration = get_video_duration(file_location)

    video = Video(
        filename=file.filename,
        path=file_location,
        upload_date=datetime.utcnow(),
        duration=duration,
        status="Processing",
    )
    db.add(video)
    db.commit()
    db.refresh(video)

    background_tasks.add_task(simulate_video_processing, video_id=video.id, db=db)

    return {
        "id": video.id,
        "filename": video.filename,
        "upload_date": video.upload_date,
        "duration": video.duration,
    }

@router.get("/", response_model=list[VideoRead])
def read_videos(db: Session = Depends(get_db)):
    videos = db.query(Video).options(
    joinedload(Video.video_tags).joinedload(AthleteVideoTag.video)
    ).all()
    
    # Flatten tagged videos
    for video in videos:
        video.athletes = [tag.athlete for tag in video.video_tags]

    return videos

@router.get("/by-athlete/{athlete_id}", response_model=list[NestedVideoRead])
def read_videos(
    athlete_id: int,
    db: Session = Depends(get_db)
):
    videos = (
        db.query(Video)
        .join(AthleteVideoTag, Video.id == AthleteVideoTag.video_id)
        .options(joinedload(Video.video_tags)) 
        .filter(AthleteVideoTag.athlete_id == athlete_id)
        .all()
    )
    return videos

def get_video_duration(path: str) -> float | None:
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        path,
    ]
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        duration = float(result.stdout.strip())
        return duration
    except Exception as e:
        print(f"Error getting duration: {e}")
        return None
    
def simulate_video_processing(video_id: int, db: Session):
    time.sleep(40)  # simulate processing time
    video = db.query(Video).get(video_id)
    if video:
        video.status = "Complete"
        db.commit()

@router.get("/stream/{filename}")
def stream_video(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    return FileResponse(path=file_path, media_type="video/mp4")


@router.get("/{video_id}", response_model=NestedVideoRead)
def get_video_info(video_id: int, db: Session = Depends(get_db)):
    video = (
        db.query(Video)
        .filter(Video.id == video_id)
        .first()
    )

    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    return video
   