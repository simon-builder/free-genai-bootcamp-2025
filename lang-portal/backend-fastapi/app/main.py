from fastapi import FastAPI
from app.models import Base
from app.database import engine
from app.routers import words

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the words router
app.include_router(words.router)