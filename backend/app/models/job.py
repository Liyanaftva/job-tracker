from sqlalchemy import Column, Integer, String, Text, DateTime, ARRAY
from sqlalchemy.sql import func
from app.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    
    # Basic job info (manual entry)
    title = Column(String(200), nullable=False)
    company = Column(String(200), nullable=False)
    location = Column(String(200), nullable=True)
    job_description = Column(Text, nullable=False)  # raw JD text you paste
    
    # Application tracking
    status = Column(String(50), default="Applied")  
    # values: Applied, Interview, Offer, Rejected
    applied_date = Column(DateTime, server_default=func.now())
    notes = Column(Text, nullable=True)
    
    # AI-generated fields (filled by Groq)
    jd_summary = Column(Text, nullable=True)
    required_skills = Column(ARRAY(String), nullable=True)   # extracted from JD
    skill_gaps = Column(ARRAY(String), nullable=True)        # missing from your resume
    resume_suggestions = Column(Text, nullable=True)
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())