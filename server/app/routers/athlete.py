from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Athlete, AthleteVideoTag, AthleteVideoMetric
from app.schemas.athlete import AthleteCreate, AthleteRead
from app.schemas.nested_athlete import NestedAthleteRead
from collections import defaultdict
from typing import Dict
from app.database import get_db
from sqlalchemy.orm import joinedload

router = APIRouter(prefix="/athletes", tags=["Athletes"])


@router.post("/", response_model=AthleteRead)
def create_athlete(athlete: AthleteCreate, db: Session = Depends(get_db)):
    db_athlete = Athlete(**athlete.dict())
    db.add(db_athlete)
    db.commit()
    db.refresh(db_athlete)
    return db_athlete

@router.get("/", response_model=list[AthleteRead])
def read_athletes(db: Session = Depends(get_db)):
    athletes = db.query(Athlete).options(
    joinedload(Athlete.video_tags).joinedload(AthleteVideoTag.video)
    ).all()
    
    for athlete in athletes:
        athlete.videos = [tag.video for tag in athlete.video_tags]

    return athletes

@router.get("/{athlete_id}", response_model=AthleteRead)
def read_athlete(athlete_id: int, db: Session = Depends(get_db)):
    athlete = db.query(Athlete).options(
    joinedload(Athlete.video_tags).joinedload(AthleteVideoTag.video)
    ).filter(Athlete.id == athlete_id).first()
    if not athlete:
        raise HTTPException(status_code=404, detail="Athlete not found")

    athlete.videos = [tag.video for tag in athlete.video_tags]

    return athlete

@router.delete("/{athlete_id}", status_code=204)
def delete_athlete(athlete_id: int, db: Session = Depends(get_db)):
    athlete = db.query(Athlete).get(athlete_id)
    if not athlete:
        raise HTTPException(status_code=404, detail="Athlete not found")
    db.delete(athlete)
    db.commit()
    return {"message": "Athlete deleted"}

@router.put("/{athlete_id}", response_model=AthleteRead)
def update_athlete(athlete_id: int, updated: AthleteCreate, db: Session = Depends(get_db)):
    athlete = db.query(Athlete).get(athlete_id)
    if not athlete:
        raise HTTPException(status_code=404, detail="Athlete not found")
    
    for key, value in updated.dict().items():
        setattr(athlete, key, value)
    
    db.commit()
    db.refresh(athlete)
    return athlete


@router.get("/by-video/{video_id}", response_model=list[NestedAthleteRead])
def read_athletes_in_video(
    video_id: int,
    db: Session = Depends(get_db)
):
    athletes = (
        db.query(Athlete)
        .join(AthleteVideoTag, Athlete.id == AthleteVideoTag.athlete_id)
        .filter(AthleteVideoTag.video_id == video_id)
        .all()
    )
    return athletes

@router.get("/{athlete_id}/performance-summary")
def athlete_performance_summary(athlete_id: int, db: Session = Depends(get_db)) -> Dict[str, float]:
    metrics = db.query(AthleteVideoMetric).filter(AthleteVideoMetric.athlete_id == athlete_id).all()

    if not metrics:
        raise HTTPException(status_code=404, detail="No metrics found for this athlete")

    sums = defaultdict(float)
    counts = defaultdict(int)

    for metric in metrics:
        sums[metric.metric_type] += float(metric.metric_value)
        counts[metric.metric_type] += 1

    averages = {metric_type: sums[metric_type] / counts[metric_type] for metric_type in sums}

    return averages