# app/create_tables.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 👈 MUST COME FIRST

from app.database import Base, engine
from app.models import user, mood

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
