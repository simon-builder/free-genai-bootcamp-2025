from pydantic import BaseModel

class StudyActivityCreate(BaseModel):
    name: str
    url: str
    preview_url: str | None = None  # Optional field

class StudyActivity(StudyActivityCreate):
    id: int

    class Config:
        from_attributes = True