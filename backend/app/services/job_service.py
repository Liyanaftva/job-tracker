from sqlalchemy.orm import Session
from app.models.job import Job
from app.schemas.job import JobCreate, JobUpdate

def create_job(db: Session, job_data: JobCreate):
    new_job = Job(
        title=job_data.title,
        company=job_data.company,
        location=job_data.location,
        job_description=job_data.job_description,
        notes=job_data.notes
    )
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

def get_all_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Job).offset(skip).limit(limit).all()

def get_job_by_id(db: Session, job_id: int):
    return db.query(Job).filter(Job.id == job_id).first()

def update_job(db: Session, job_id: int, job_data: JobUpdate):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        return None
    if job_data.status is not None:
        job.status = job_data.status
    if job_data.notes is not None:
        job.notes = job_data.notes
    db.commit()
    db.refresh(job)
    return job

def delete_job(db: Session, job_id: int):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        return None
    db.delete(job)
    db.commit()
    return True

def update_job_ai_fields(db: Session, job_id: int, ai_data: dict):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        return None
    job.jd_summary = ai_data.get("jd_summary")
    job.required_skills = ai_data.get("required_skills")
    job.skill_gaps = ai_data.get("skill_gaps")
    job.resume_suggestions = ai_data.get("resume_suggestions")
    db.commit()
    db.refresh(job)
    return job