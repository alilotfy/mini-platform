from pydantic import BaseModel
from typing import List
from app.schemas.video import NestedVideoRead

class AthleteBase(BaseModel):
    name: str
    sport: str
    age: int

class AthleteCreate(AthleteBase):
    pass

class AthleteRead(AthleteBase):
    id: int
    videos: List[NestedVideoRead] = []

    class Config:
        orm_mode = True
