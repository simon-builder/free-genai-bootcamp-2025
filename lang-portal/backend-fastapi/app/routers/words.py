from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.schemas.words import WordCreate

router = APIRouter(
    prefix="/words",
    tags=["words"]
)

@router.get("")
def get_words(
    page: int = 1,
    sort_by: str = "kanji",
    order: str = "asc",
    db: Session = Depends(get_db)
):
    # Validate sort field
    valid_sort_fields = ['kanji', 'romaji', 'english', 'correct_count', 'wrong_count']
    if sort_by not in valid_sort_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Must be one of: {valid_sort_fields}")
    
    # Validate order
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Order must be 'asc' or 'desc'")
    
    # Calculate offset
    limit = 10  # items per page
    offset = (page - 1) * limit
    
    # Build query
    query = db.query(models.Word)
    
    # Apply sorting
    if order == 'asc':
        query = query.order_by(getattr(models.Word, sort_by).asc())
    else:
        query = query.order_by(getattr(models.Word, sort_by).desc())
    
    # Apply pagination
    words = query.offset(offset).limit(limit).all()
    
    return words

@router.get("/{word_id}")
def get_word(word_id: int, db: Session = Depends(get_db)):
    word = db.query(models.Word).filter(models.Word.id == word_id).first()
    if not word:
        raise HTTPException(status_code=404, detail="Word not found")
    return word

@router.post("")
def create_word(
    word: WordCreate,
    db: Session = Depends(get_db)
):
     # Convert Pydantic model to dict
    word_data = word.model_dump()
    
    # Create SQLAlchemy model instance with dict data
    db_word = models.Word(**word_data)
    
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word