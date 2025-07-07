from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr

class MoodCreate(BaseModel):
    mood: str
    note: Optional[str] = None
    user_id: int

class MoodResponse(BaseModel):
    id: int
    mood: str
    note: Optional[str]
    timestamp: datetime

    class Config:
        orm_mode = True
