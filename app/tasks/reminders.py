from app.celery_app import celery_app
from app.db.session import SessionLocal
from app.models.user import User
from app.mqtt.publisher import publish_reminder

@celery_app.task
def remind_user_to_log_mood():
    db = SessionLocal()
    try:
        users = db.query(User.id).all()
        for (user_id,) in users:
            publish_reminder(user_id, "Hey! Don't forget to log your mood today!")
    finally:
        db.close()

@celery_app.task(name="app.tasks.reminders.send_mood_reminder_task")
def send_mood_reminder_task():
    print("Celery Task started: send_mood_reminder_task")
    try:
        publish_reminder(1, "Reminder: Please log your mood.")
        print("MQTT message sent")
    except Exception as e:
        print("Error sending MQTT:", e)
