from celery import Celery
from dotenv import load_dotenv
import os
from celery.schedules import crontab

load_dotenv()

REDIS_URL = os.getenv("REDIS_BROKER_URL")
if not REDIS_URL:
    raise ValueError("REDIS_BROKER_URL not found in .env")

celery_app = Celery(
    "worker",
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=["app.tasks.reports", "app.tasks.reminders"]
)

celery_app.conf.task_routes = {
    "app.tasks.reports.generate_report_task": {"queue": "reports"},
    "app.tasks.reminders.remind_user_to_log_mood": {"queue": "reminders"},
    "app.tasks.reminders.remind_user_reports": {"queue": "reminders"},
    "app.tasks.reminders.send_mood_reminder_task": {"queue": "reminders"},
}

celery_app.conf.update(
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    timezone='Asia/Kolkata',
    enable_utc=False,
)

celery_app.conf.beat_schedule = {
    'send-mood-reminder-every-3-minutes': {
        'task': 'app.tasks.reminders.send_mood_reminder_task',
        'schedule': crontab(minute='*'),
        'options': {'queue': 'reminders'},
    },
}

celery_app.conf.broker_connection_retry_on_startup = True
celery_app.conf.broker_transport_options = {
    'max_retries': 3,
    'interval_start': 0,
    'interval_step': 0.5,
    'interval_max': 1,
    'socket_timeout': 10,
}

