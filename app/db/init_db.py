from sqlalchemy.orm import Session
from .session import engine
from app.models import user, mood, report  # Ensure all models are imported

def init_db():
    user.Base.metadata.create_all(bind=engine)
    mood.Base.metadata.create_all(bind=engine)
    report.Base.metadata.create_all(bind=engine)
