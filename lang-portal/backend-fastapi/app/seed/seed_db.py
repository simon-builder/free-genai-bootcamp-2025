from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base, Word, StudyActivity, Group
import json

def clean_db():
    # Drop all tables
    Base.metadata.drop_all(bind=engine)
    # Recreate all tables
    Base.metadata.create_all(bind=engine)

def load_json(filename: str):
    with open(f"app/seed/{filename}", "r", encoding="utf-8") as f:
        return json.load(f)

def seed_db(db=None):
    should_close_db = False
    if db is None:
        # Create database engine and session if none provided
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        should_close_db = True
    
    try:
        print("Creating groups...")
        # Create verb and adjective groups
        verb_group = Group(name="verb")
        adj_group = Group(name="adjective")
        db.add(verb_group)
        db.add(adj_group)
        db.flush()  # This ensures the groups get their IDs
        print(f"Created groups with IDs: verb={verb_group.id}, adj={adj_group.id}")

        # Load and insert verbs
        verbs = load_json("data_verbs.json")
        for verb in verbs:
            word = Word(
                kanji=verb["kanji"],
                romaji=verb["romaji"],
                english=verb["english"],
                parts=verb["parts"]
            )
            word.groups.append(verb_group)  # Associate with verb group
            db.add(word)

        # Load and insert adjectives
        adjectives = load_json("data_adjectives.json")
        for adj in adjectives:
            word = Word(
                kanji=adj["kanji"],
                romaji=adj["romaji"],
                english=adj["english"],
                parts=adj["parts"]
            )
            word.groups.append(adj_group)  # Associate with adjective group
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
        
        # Verify after commit
        groups = db.query(Group).all()
        print(f"After seeding, found groups: {[g.name for g in groups]}")
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
        raise
    finally:
        if should_close_db:
            db.close()

if __name__ == "__main__":
    print("Cleaning database...")
    clean_db()
    print("Seeding database...")
    seed_db()
    print("Done!") 