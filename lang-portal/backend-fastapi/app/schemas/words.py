from pydantic import BaseModel

class WordCreate(BaseModel):
    kanji: str
    romaji: str
    english: str
    parts: dict

class Word(WordCreate):
    id: int
    correct_count: int = 0
    wrong_count: int = 0

    class Config:
        from_attributes = True