from fastapi import APIRouter, Depends
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