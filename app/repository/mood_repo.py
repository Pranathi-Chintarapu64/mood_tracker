from sqlalchemy.orm import Session
from app.models.mood import Mood
from app.api.schemas import MoodCreate

def log_mood(db: Session, mood_data: MoodCreate):
    mood = Mood(**mood_data.dict())
    db.add(mood)
    db.commit()
    db.refresh(mood)
    return mood
