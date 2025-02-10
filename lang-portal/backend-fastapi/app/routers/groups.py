from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc, asc
from app.database import get_db
from app import models
from app.schemas.groups import GroupCreate, Group, GroupWithWords
from typing import Literal

router = APIRouter(
    prefix="/groups",
    tags=["groups"]
)

@router.get("/{group_id}")
def get_group(
    group_id: int,
    page: int = 1,
    sort_by: Literal["kanji", "romaji", "english"] = "kanji",
    order: Literal["asc", "desc"] = "asc",
    db: Session = Depends(get_db)
):
    # Get the group
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    
    # Calculate pagination for words
    limit = 10
    offset = (page - 1) * limit
    
    # Query words through the relationship with sorting
    query = db.query(models.Word)\
        .join(models.word_groups)\
        .filter(models.word_groups.c.group_id == group_id)
    
    # Apply sorting
    if order == "asc":
        query = query.order_by(asc(getattr(models.Word, sort_by)))
    else:
        query = query.order_by(desc(getattr(models.Word, sort_by)))
    
    # Apply pagination
    words = query.offset(offset).limit(limit).all()
    
    return {
        "id": group.id,
        "name": group.name,
        "words_count": group.words_count,
        "words": words
    }

@router.post("/{group_id}/words/{word_id}")
def add_word_to_group(
    group_id: int,
    word_id: int,
    db: Session = Depends(get_db)
):
    # Verify group exists
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    
    # Verify word exists
    word = db.query(models.Word).filter(models.Word.id == word_id).first()
    if not word:
        raise HTTPException(status_code=404, detail="Word not found")
    
    # Add word to group
    group.words.append(word)
    group.words_count = len(group.words)  # Update word count
    db.commit()
    
    return {"status": "success", "message": "Word added to group"}