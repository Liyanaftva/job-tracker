from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# What the USER SENDS when creating a job (input)
class JobCreate(BaseModel):
    title: str
    company: str
    location: Optional[str] = None
    job_description: str
    notes: Optional[str] = None

# What WE SEND BACK to the frontend (output)
class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    location: Optional[str] = None
    job_description: str
    status: str
    notes: Optional[str] = None

    # AI generated fields
    jd_summary: Optional[str] = None
    required_skills: Optional[List[str]] = None
    skill_gaps: Optional[List[str]] = None
    resume_suggestions: Optional[str] = None

    applied_date: Optional[datetime] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# What the user sends when UPDATING a job
class JobUpdate(BaseModel):
    status: Optional[str] = None
    notes: Optional[str] = None