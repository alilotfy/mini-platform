from pydantic import BaseModel

class AthleteVideoTagCreate(BaseModel):
    athlete_id: int
    video_id: int