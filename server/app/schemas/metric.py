
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MetricBase(BaseModel):
    athlete_id: int
    video_id: int
    metric_type: str
    metric_value: float
    timestamp: float

class MetricCreate(MetricBase):
    pass

class MetricUpdate(BaseModel):
    metric_type: Optional[str]
    metric_value: Optional[float]
    timestamp: Optional[float]

class MetricRead(MetricBase):
    id: int

    class Config:
        orm_mode = True