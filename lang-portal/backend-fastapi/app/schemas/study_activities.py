from pydantic import BaseModel, ConfigDict

class StudyActivityCreate(BaseModel):
    name: str
    url: str
    preview_url: str | None = None  # Optional field

class StudyActivity(StudyActivityCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)