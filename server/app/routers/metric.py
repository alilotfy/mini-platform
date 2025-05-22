# app/routers/metric.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import AthleteVideoMetric
from app.schemas.metric import MetricCreate, MetricUpdate, MetricRead

router = APIRouter(prefix="/metrics", tags=["Metrics"])

@router.post("/", response_model=MetricRead)
def create_metric(metric: MetricCreate, db: Session = Depends(get_db)):
    db_metric = AthleteVideoMetric(**metric.dict())
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db_metric

from typing import Optional

@router.get("/by-athlete-video/", response_model=list[MetricRead])
def get_metrics(
    athlete_id: Optional[int] = None,
    video_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    query = db.query(AthleteVideoMetric)
    if athlete_id is not None:
        query = query.filter(AthleteVideoMetric.athlete_id == athlete_id)
    if video_id is not None:
        query = query.filter(AthleteVideoMetric.video_id == video_id)
    return query.all()

@router.put("/{metric_id}", response_model=MetricRead)
def update_metric(metric_id: int, metric: MetricUpdate, db: Session = Depends(get_db)):
    db_metric = db.query(AthleteVideoMetric).get(metric_id)
    if not db_metric:
        raise HTTPException(status_code=404, detail="Metric not found")
    for key, value in metric.dict(exclude_unset=True).items():
        setattr(db_metric, key, value)
    db.commit()
    db.refresh(db_metric)
    return db_metric

@router.delete("/{metric_id}")
def delete_metric(metric_id: int, db: Session = Depends(get_db)):
    db_metric = db.query(AthleteVideoMetric).get(metric_id)
    if not db_metric:
        raise HTTPException(status_code=404, detail="Metric not found")
    db.delete(db_metric)
    db.commit()
    return {"message": "Metric deleted"}

@router.get("/by-video/{video_id}", response_model=list[MetricRead])
def get_metrics_by_video(
    video_id: int,
    db: Session = Depends(get_db)):

    metrics = db.query(AthleteVideoMetric).filter(AthleteVideoMetric.video_id == video_id).all()
    return metrics