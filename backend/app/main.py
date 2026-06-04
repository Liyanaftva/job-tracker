# app/main.py
from fastapi import FastAPI
from app.database import engine, Base
from app import models  # triggers table creation

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Tracker API")

@app.get("/")
def root():
    return {"message": "Job Tracker API is running"}