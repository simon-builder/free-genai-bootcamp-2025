from pydantic import BaseModel
from datetime import datetime

class StudySessionCreate(BaseModel):
    group_id: int
    study_activity_id: int

class StudySession(StudySessionCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True