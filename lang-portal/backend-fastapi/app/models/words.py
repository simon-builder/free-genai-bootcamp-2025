from sqlalchemy import Column, Integer, String
from app.database import Base
import json

class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)
    kanji = Column(String, nullable=False)
    romaji = Column(String, nullable=False)
    english = Column(String, nullable=False)
    parts = Column(String, nullable=False)  # Store as JSON string
    
    # Add many-to-many relationship
    groups = relationship("Group", secondary=word_groups, back_populates="words")
    review_items = relationship("WordReviewItem", back_populates="word")

    def __init__(self, **kwargs):
        # Convert parts dict to JSON string before storing
        if 'parts' in kwargs:
            kwargs['parts'] = json.dumps(kwargs['parts'])
        super().__init__(**kwargs)