from pydantic import BaseModel, ConfigDict
from typing import List
from .words import WordCreate

class GroupCreate(BaseModel):
    name: str

class Group(GroupCreate):
    id: int
    words_count: int
    model_config = ConfigDict(from_attributes=True)

class GroupWithWords(Group):
    words: List[WordCreate]
    model_config = ConfigDict(from_attributes=True)