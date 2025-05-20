from sqlalchemy import Column, Integer, String
from app.database import Base  # assumes you have Base defined in database.py

class Athlete(Base):
    __tablename__ = "Athlete"

    id = Column(Integer, primary_key=True, index=True)  # Unique ID
    name = Column(String, index=True)
    sport = Column(String, index=True)
    age = Column(Integer)
