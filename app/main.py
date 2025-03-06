from fastapi import FastAPI
from sqlalchemy.orm import Session
from app.database import SessionLocal

app = FastAPI(
    title="Bike Maintenance API",
    description="API for managing bikes, services, fuel logs, reminders, etc.",
    version="1.0.0"
)


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Bike Maintenance API is running with MySQL!"}

@app.get("/healthy")
def hello():
    return {"status": "healthy"}