# app/main.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.api import routes

app = FastAPI()
app.include_router(routes.router)

@app.get("/")
def test_connection(db: Session = Depends(get_db)):
    return {"message": "Database connected successfully"}
