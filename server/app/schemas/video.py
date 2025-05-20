from pydantic import BaseModel
from typing import List
from app.schemas.nested_athlete import NestedAthleteRead

class VideoCreate(BaseModel):
    filename: str

class NestedVideoRead(VideoCreate):
    id: int
    path: str

    class Config:
        orm_mode = True


class VideoRead(NestedVideoRead):
    athletes: List[NestedAthleteRead] = []

    class Config:
        orm_mode = True