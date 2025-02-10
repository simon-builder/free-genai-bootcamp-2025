from pydantic import BaseModel
from typing import Dict

class WordCreate(BaseModel):
    kanji: str
    romaji: str
    english: str
    parts: Dict