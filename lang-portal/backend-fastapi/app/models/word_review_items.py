from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class WordReviewItem(Base):
    __tablename__ = "word_review_items"

    id = Column(Integer, primary_key=True, index=True)
    word_id = Column(Integer, ForeignKey("words.id"), nullable=False)
    study_session_id = Column(Integer, ForeignKey("study_sessions.id"), nullable=False)
    correct = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    word = relationship("Word", back_populates="review_items")
    study_session = relationship("StudySession", back_populates="review_items")