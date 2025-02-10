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