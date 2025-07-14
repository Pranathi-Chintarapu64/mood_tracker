from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.user import User
from app.dependencies import get_current_user
from app.tasks.reports import generate_report_task
from app.models.report import Report
import os
from fastapi.responses import FileResponse
from app.schemas.report import ReportOut
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/generate")
def generate_report(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Create a new Report record with 'pending' status
    report = Report(user_id=current_user.id, file_path="pending")
    db.add(report)
    db.commit()
    db.refresh(report)

    generate_report_task.apply_async(args=[report.id])

    return {
        "message": "Report generation started",
        "report_id": report.id
    }

@router.get("/download/{report_id}")
def download_report(report_id: int, current_user: User = Depends(get_current_user)):
    db = SessionLocal()
    try:
        report = db.query(Report).filter(Report.id == report_id, Report.user_id == current_user.id).first()
        if not report or not os.path.exists(report.file_path):
            raise HTTPException(status_code=404, detail="Report not found")

        return FileResponse(report.file_path, media_type="application/pdf", filename=os.path.basename(report.file_path))
    finally:
        db.close()

@router.get("/list", response_model=List[ReportOut])
def list_reports(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Report).filter(Report.user_id == current_user.id).order_by(Report.created_at.desc()).all()

@router.get("/latest", response_model=ReportOut)
def latest_report(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    report = db.query(Report).filter(Report.user_id == current_user.id).order_by(Report.created_at.desc()).first()
    if not report:
        raise HTTPException(status_code=404, detail="No reports found")
    return report
