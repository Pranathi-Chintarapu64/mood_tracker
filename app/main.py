from fastapi import FastAPI
from app.models import user as user_model, mood as mood_model, report as report_model
from app.routes import user as user_routes, mood as mood_routes, report as report_routes
from app.db.session import engine
from app import models
from app.tasks import reports
from app.routes import reminders


app = FastAPI()

app.include_router(user_routes.router, prefix="/api/user")
app.include_router(mood_routes.router, prefix="/api/mood")
app.include_router(report_routes.router, prefix="/api/report")
app.include_router(reminders.router, prefix="/reminders", tags=["Reminders"])


user_model.Base.metadata.create_all(bind=engine)
mood_model.Base.metadata.create_all(bind=engine)
report_model.Base.metadata.create_all(bind=engine)
