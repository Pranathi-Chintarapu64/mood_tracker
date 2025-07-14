from app.db.session import engine, Base
from app.models import user, mood, report

print("Creating all tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully.")
