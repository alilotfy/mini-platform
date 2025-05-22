from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float,UniqueConstraint
from app.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Athlete(Base):    
    __tablename__ = "Athlete"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    sport = Column(String)
    age = Column(Integer)

    video_tags = relationship("AthleteVideoTag", back_populates="athlete")


class Video(Base):
    __tablename__ = "Video"

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    path = Column(String)
    upload_date = Column(DateTime)
    duration = Column(Float)
    status = Column(String) 

    video_tags = relationship("AthleteVideoTag", back_populates="video")
    athlete_video_metrics = relationship("AthleteVideoMetric", back_populates="video")


class AthleteVideoTag(Base):
    __tablename__ = "AthleteVideoTag"

    id = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, ForeignKey("Athlete.id"))
    video_id = Column(Integer, ForeignKey("Video.id"))

    athlete = relationship("Athlete", back_populates="video_tags")
    video = relationship("Video", back_populates="video_tags")
    __table_args__ = (
        UniqueConstraint('athlete_id', 'video_id', name='uix_athlete_video'),
    )


class AthleteVideoMetric(Base):
    __tablename__ = "AthleteVideoMetric"

    id = Column(Integer, primary_key=True, index=True)
    athlete_id = Column(Integer, ForeignKey("Athlete.id"))
    video_id = Column(Integer, ForeignKey("Video.id"))
    metric_type = Column(String, nullable=False)
    metric_value = Column(Float, nullable=False)
    timestamp = Column(Float, nullable=False)
    video = relationship("Video", back_populates="athlete_video_metrics")
