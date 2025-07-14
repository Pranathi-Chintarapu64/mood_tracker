from app.celery_app import celery_app
from app.db.session import SessionLocal
from app.models.mood import Mood
from app.models.report import Report
from app.utils.pdf import generate_pdf
from datetime import datetime
import os
from app.mqtt.client import publish_report_status
import logging

@celery_app.task
def generate_report_task(report_id: int):
    db = SessionLocal()
    try:
        report = db.query(Report).filter(Report.id == report_id).first()
        if not report:
            raise Exception("Report not found")

        moods = db.query(Mood.id, Mood.user_id, Mood.mood, Mood.created_at).filter(
            Mood.user_id == report.user_id).all()

        timestamp_str = datetime.utcnow().isoformat().replace(":", "-").replace(".", "-")
        filename = f"report_{report.user_id}_{timestamp_str}.pdf"
        filepath = os.path.join("generated_reports", filename)

        os.makedirs("generated_reports", exist_ok=True)
        print(f"[TASK] Saving PDF to {filepath} with {len(moods)} moods")
        generate_pdf(moods, filepath)
        print(f"[TASK] Report saved at {filepath}")

        # Commit
        report.file_path = filepath
        db.flush()  # ensure statement is sent
        db.commit()
        db.refresh(report)
        print(f"[TASK] DB updated for report_id={report.id} with path={report.file_path}")

        publish_report_status(report.user_id, f"Your mood report is ready. Report ID: {report.id}")
        return {"status": "completed", "report_id": report.id, "file": filepath}
    except Exception as e:
        print(f"[TASK] Error: {e}")
        publish_report_status(report.user_id, f"Error generating report: {e}")
        return {"status": "error", "message": str(e)}
    finally:
        db.close()

