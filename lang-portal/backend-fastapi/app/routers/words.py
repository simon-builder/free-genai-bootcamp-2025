from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func, desc, asc, case
from sqlalchemy.orm import Session, joinedload
from app.database import get_db
from app import models
from app.schemas.words import WordCreate, Word
from typing import Literal

router = APIRouter(
    prefix="/words",
    tags=["words"]
)

@router.get("")
def get_words(
    page: int = 1,
    sort_by: Literal["kanji", "romaji", "english", "correct_count", "wrong_count"] = "kanji",
    order: Literal["asc", "desc"] = "asc",
    db: Session = Depends(get_db)
):
    # Calculate pagination
    limit = 10
    offset = (page - 1) * limit
    
    # Base query with review statistics
    query = db.query(
        models.Word,
        func.count(case(
            (models.WordReviewItem.correct == True, 1),
            else_=None
        )).label('correct_count'),
        func.count(case(
            (models.WordReviewItem.correct == False, 1),
            else_=None
        )).label('wrong_count')
    ).outerjoin(
        models.WordReviewItem
    ).options(
        joinedload(models.Word.groups)
    ).group_by(
        models.Word.id
    )
    
    # Apply sorting
    if sort_by in ["kanji", "romaji", "english"]:
        # Direct column sorting
        if order == "asc":
            query = query.order_by(asc(getattr(models.Word, sort_by)))
        else:
            query = query.order_by(desc(getattr(models.Word, sort_by)))
    else:
        # Review statistics sorting
        if order == "asc":
            query = query.order_by(asc(sort_by))
        else:
            query = query.order_by(desc(sort_by))
    
    # Apply pagination
    results = query.offset(offset).limit(limit).all()
    
    # Format response with groups
    words = []
    for word, correct, wrong in results:
        word_dict = {
            "id": word.id,
            "kanji": word.kanji,
            "romaji": word.romaji,
            "english": word.english,
            "parts": word.parts,
            "correct_count": correct,
            "wrong_count": wrong,
            "groups": [{"id": g.id, "name": g.name} for g in word.groups]
        }
        words.append(word_dict)
    
    return words

@router.get("/{word_id}")
def get_word(word_id: int, db: Session = Depends(get_db)):
    # Query word with review statistics
    result = db.query(
        models.Word,
        func.count(case(
            (models.WordReviewItem.correct == True, 1),
            else_=None
        )).label('correct_count'),
        func.count(case(
            (models.WordReviewItem.correct == False, 1),
            else_=None
        )).label('wrong_count')
    ).outerjoin(
        models.WordReviewItem
    ).options(
        joinedload(models.Word.groups)
    ).filter(
        models.Word.id == word_id
    ).group_by(
        models.Word.id
    ).first()
    
    if not result:
        raise HTTPException(status_code=404, detail="Word not found")
    
    word, correct, wrong = result
    
    # Try to parse JSON string to dict if it's a string
    parts = word.parts
    if isinstance(parts, str):
        import json
        try:
            parts = json.loads(parts)
        except json.JSONDecodeError:
            parts = {}
    
    return {
        "id": word.id,
        "kanji": word.kanji,
        "romaji": word.romaji,
        "english": word.english,
        "parts": parts,
        "correct_count": correct,
        "wrong_count": wrong,
        "groups": [{"id": g.id, "name": g.name} for g in word.groups]
    }