from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.db.session import engine, Base


class Mood(Base):
    __tablename__ = "moods"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    mood = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)



