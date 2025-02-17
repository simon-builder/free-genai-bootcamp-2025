from pydantic import BaseModel, ConfigDict

class WordBase(BaseModel):
    kanji: str
    romaji: str
    english: str
    parts: dict

    # New style using ConfigDict
    model_config = ConfigDict(from_attributes=True)

class Word(WordBase):
    id: int
    correct_count: int = 0
    wrong_count: int = 0

class WordCreate(WordBase):
    pass