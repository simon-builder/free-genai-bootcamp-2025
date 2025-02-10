""" from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Base
from app.database import engine, get_db
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Create a group
@app.post("/groups")
def create_group(name: str, db: Session = Depends(get_db)):
    group = models.Group(name=name)
    db.add(group)
    db.commit()
    db.refresh(group)
    return group

# Get all groups
@app.get("/groups")
def get_groups(db: Session = Depends(get_db)):
    groups = db.query(models.Group).all()
    return groups

# Get a specific group
@app.get("/groups/{group_id}")
def get_group(group_id: int, db: Session = Depends(get_db)):
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group """