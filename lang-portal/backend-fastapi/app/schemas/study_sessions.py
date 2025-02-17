from pydantic import BaseModel, ConfigDict
from datetime import datetime

class StudySessionCreate(BaseModel):
    group_id: int
    study_activity_id: int

class StudySession(StudySessionCreate):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class WordReviewCreate(BaseModel):
    word_id: int
    correct: bool