from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import AthleteVideoTag
from app.schemas.athelete_video_tag import AthleteVideoTagCreate
from app.database import get_db

router = APIRouter(prefix="/tags", tags=["Athlete Tags"])


@router.post("/")
def tag_athlete(data: AthleteVideoTagCreate, db: Session = Depends(get_db)):
    tag = AthleteVideoTag(**data.dict())
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag


@router.delete("/")
def delete_athlete_video_tag(athlete_id: int, video_id: int, db: Session = Depends(get_db)):
    tag = db.query(AthleteVideoTag).filter_by(athlete_id=athlete_id, video_id=video_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    db.delete(tag)
    db.commit()
    return {"message": "Tag deleted successfully"}