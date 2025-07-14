from fastapi import APIRouter
from app.tasks.reminders import send_mood_reminder_task, remind_user_to_log_mood

router = APIRouter()

@router.post("/test-reminder/")
def trigger_reminder():
    send_mood_reminder_task.delay()
    return {"message": "Test reminder triggered"}


@router.post("/remind-all/")
def trigger_reminders_for_all():
    remind_user_to_log_mood.delay()
    return {"message": "Reminders for all users triggered"}
