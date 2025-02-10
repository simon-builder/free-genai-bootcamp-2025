from pydantic import BaseModel
from typing import List
from .words import WordCreate

class GroupCreate(BaseModel):
    name: str

class Group(GroupCreate):
    id: int
    words_count: int

    class Config:
        from_attributes = True

class GroupWithWords(Group):
    words: List[WordCreate]

    class Config:
        from_attributes = True