from fastapi import FastAPI
from app.models import Base
from app.database import engine
from app.routers import words, study_activities

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(words.router)
app.include_router(study_activities.router)