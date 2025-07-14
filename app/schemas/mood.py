from pydantic import BaseModel
from datetime import datetime

class MoodCreate(BaseModel):
    mood: str

class MoodOut(MoodCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
