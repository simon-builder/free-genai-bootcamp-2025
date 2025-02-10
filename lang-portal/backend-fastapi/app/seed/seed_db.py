from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base, Word, StudyActivity
import json

def clean_db():
    # Drop all tables
    Base.metadata.drop_all(bind=engine)
    # Recreate all tables
    Base.metadata.create_all(bind=engine)

def load_json(filename: str):
    with open(f"app/seed/{filename}", "r", encoding="utf-8") as f:
        return json.load(f)

def seed_db():
    db = SessionLocal()
    try:
        # Load and insert verbs
        verbs = load_json("data_verbs.json")
        for verb in verbs:
            word = Word(
                kanji=verb["kanji"],
                romaji=verb["romaji"],
                english=verb["english"],
                parts=verb["parts"],
                type="verb"
            )
            db.add(word)

        # Load and insert adjectives
        adjectives = load_json("data_adjectives.json")
        for adj in adjectives:
            word = Word(
                kanji=adj["kanji"],
                romaji=adj["romaji"],
                english=adj["english"],
                parts=adj["parts"],
                type="adjective"
            )
            db.add(word)

        # Load and insert study activities
        activities = load_json("study_activities.json")
        for activity in activities:
            study_activity = StudyActivity(
                name=activity["name"],
                url=activity["url"],
                preview_url=activity["preview_url"]
            )
            db.add(study_activity)

        db.commit()
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    print("Cleaning database...")
    clean_db()
    print("Seeding database...")
    seed_db()
    print("Done!") 