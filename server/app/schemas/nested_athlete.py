from pydantic import BaseModel

class NestedAthleteRead(BaseModel):
    name: str
    sport: str
    age: int
    id: int
    class Config:
            orm_mode = True