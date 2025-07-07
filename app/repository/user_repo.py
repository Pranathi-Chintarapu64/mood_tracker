from sqlalchemy.orm import Session
from app.models.user import User
from app.api.schemas import UserCreate

def create_user(db: Session, user_data: UserCreate):
    user = User(username=user_data.username, email=user_data.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
