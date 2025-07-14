import sys
import os
import logging
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(moods, filepath):
    try:
        f = StringIO()
        with redirect_stdout(f), redirect_stderr(f):  # suppress ReportLab noisy logs
            logging.warning(f"[PDF] Starting PDF generation at: {filepath}")
            c = canvas.Canvas(filepath, pagesize=letter)
            width, height = letter

            c.setFont("Helvetica-Bold", 14)
            c.drawString(50, height - 50, "Mood Report")

            c.setFont("Helvetica", 12)
            y = height - 100

            if not moods:
                c.drawString(50, y, "No mood entries found.")
            else:
                for mood in moods:
                    mood_text = f"Date: {mood.created_at.strftime('%Y-%m-%d %H:%M:%S')} | Mood: {mood.mood}"
                    c.drawString(50, y, mood_text)
                    y -= 20
                    if y < 50:
                        c.showPage()
                        c.setFont("Helvetica", 12)
                        y = height - 50

            c.save()
            logging.warning(f"[PDF] PDF generated successfully: {filepath}")
    except Exception as e:
        logging.error(f"Failed to generate PDF: {e}")
        raise
