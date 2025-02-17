import pytest
import warnings

# Filter out warnings from starlette.formparsers
# Must be before any imports that might trigger the warning
warnings.filterwarnings(
    "ignore",
    module="starlette.formparsers"
)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.main import app
from app.seed.seed_db import seed_db
from fastapi.testclient import TestClient

# Use an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db():
    # Create tables for each test
    Base.metadata.create_all(bind=engine)
    connection = engine.connect()
    # Begin a non-ORM transaction
    transaction = connection.begin()
    
    # Create session bound to this connection
    session = TestingSessionLocal(bind=connection)
    
    try:
        seed_db(session)  # Seed data
        yield session
    finally:
        session.close()
        # Rollback the transaction
        transaction.rollback()
        # Close the connection
        connection.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            pass
    
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear() 