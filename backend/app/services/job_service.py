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

def get_all_jobs(db: Session):
    return db.query(Job).all()

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