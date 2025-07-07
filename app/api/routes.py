from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.api.schemas import UserCreate, MoodCreate, MoodResponse
from app.repository import user_repo, mood_repo

router = APIRouter()

@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_repo.create_user(db, user)

@router.post("/mood/log", response_model=MoodResponse)
def log_user_mood(mood: MoodCreate, db: Session = Depends(get_db)):
    return mood_repo.log_mood(db, mood)
