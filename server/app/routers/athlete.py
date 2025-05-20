from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Athlete
from app.schemas.athlete import AthleteCreate, AthleteRead
from app.database import get_db

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
    return db.query(Athlete).all()

@router.get("/{athlete_id}", response_model=AthleteRead)
def read_athlete(athlete_id: int, db: Session = Depends(get_db)):
    athlete = db.query(Athlete).filter(Athlete.id == athlete_id).first()
    if not athlete:
        raise HTTPException(status_code=404, detail="Athlete not found")
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