from pydantic import BaseModel
from typing import List
from app.schemas.nested_athlete import NestedAthleteRead
from datetime import datetime

class VideoCreate(BaseModel):
    filename: str

class NestedVideoRead(VideoCreate):
    id: int
    path: str
    status: str
    upload_date: datetime
    class Config:
        orm_mode = True


class VideoRead(NestedVideoRead):
    athletes: List[NestedAthleteRead] = []

    class Config:
        orm_mode = True