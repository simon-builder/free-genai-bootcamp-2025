from pydantic import BaseModel, ConfigDict
from datetime import datetime

class WordReviewItemCreate(BaseModel):
    word_id: int
    study_session_id: int
    correct: bool

class WordReviewItem(WordReviewItemCreate):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)