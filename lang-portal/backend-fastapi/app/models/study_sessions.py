from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, UTC
from app.database import Base

class StudySession(Base):
    __tablename__ = "study_sessions"

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)
    study_activity_id = Column(Integer, ForeignKey("study_activities.id"), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    # Relationships
    group = relationship("Group", back_populates="study_sessions")
    study_activity = relationship("StudyActivity", back_populates="study_sessions")
    review_items = relationship("WordReviewItem", back_populates="study_session")