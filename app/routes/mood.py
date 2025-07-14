from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.mood import Mood
from app.schemas.mood import MoodCreate, MoodOut
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/log", response_model=MoodOut)
def log_mood(mood: MoodCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    mood_entry = Mood(user_id=current_user.id, mood=mood.mood)
    db.add(mood_entry)
    db.commit()
    db.refresh(mood_entry)
    return mood_entry

@router.get("/history", response_model=list[MoodOut])
def get_mood_history(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Mood).filter(Mood.user_id == current_user.id).order_by(Mood.created_at.desc()).all()


