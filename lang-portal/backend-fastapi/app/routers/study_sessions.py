from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.schemas.study_sessions import StudySessionCreate, StudySession, WordReviewCreate
from datetime import datetime

router = APIRouter(
    prefix="/study_sessions",
    tags=["study_sessions"]
)

@router.post("", response_model=StudySession)
def create_study_session(
    session: StudySessionCreate,
    db: Session = Depends(get_db)
):
    # Verify group exists
    group = db.query(models.Group).filter(models.Group.id == session.group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    
    # Verify study activity exists
    activity = db.query(models.StudyActivity).filter(models.StudyActivity.id == session.study_activity_id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Study activity not found")
    
    # Create study session
    db_session = models.StudySession(**session.model_dump())
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session

@router.post("/{session_id}/review")
def create_word_review(
    session_id: int,
    review: WordReviewCreate,
    db: Session = Depends(get_db)
):
    # Verify study session exists
    study_session = db.query(models.StudySession).filter(models.StudySession.id == session_id).first()
    if not study_session:
        raise HTTPException(status_code=404, detail="Study session not found")
    
    # Verify word exists and belongs to the session's group
    word = db.query(models.Word)\
        .join(models.word_groups)\
        .filter(
            models.Word.id == review.word_id,
            models.word_groups.c.group_id == study_session.group_id
        ).first()
    if not word:
        raise HTTPException(
            status_code=404, 
            detail="Word not found or does not belong to the session's group"
        )
    
    # Create word review
    db_review = models.WordReviewItem(
        word_id=review.word_id,
        study_session_id=session_id,
        correct=review.correct
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    
    return {"status": "success", "message": "Review recorded"}