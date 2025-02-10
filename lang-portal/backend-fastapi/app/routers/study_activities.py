from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.schemas.study_activities import StudyActivityCreate, StudyActivity

router = APIRouter(
    prefix="/study_activities",
    tags=["study_activities"]
)

@router.get("")
def get_study_activities(
    page: int = 1,
    db: Session = Depends(get_db)
):
    limit = 10
    offset = (page - 1) * limit
    activities = db.query(models.StudyActivity).offset(offset).limit(limit).all()
    return activities

@router.get("/{activity_id}")
def get_study_activity(
    activity_id: int,
    db: Session = Depends(get_db)
):
    activity = db.query(models.StudyActivity).filter(models.StudyActivity.id == activity_id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Study activity not found")
    return activity

@router.post("")
def create_study_activity(
    activity: StudyActivityCreate,
    db: Session = Depends(get_db)
):
    db_activity = models.StudyActivity(**activity.model_dump())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity