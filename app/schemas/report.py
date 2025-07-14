from pydantic import BaseModel
from datetime import datetime

class ReportOut(BaseModel):
    id: int
    file_path: str
    created_at: datetime

    class Config:
        orm_mode = True
