from pydantic import BaseModel

class AthleteBase(BaseModel):
    name: str
    sport: str
    age: int

class AthleteCreate(AthleteBase):
    pass

class AthleteRead(AthleteBase):
    id: int

    class Config:
        orm_mode = True
