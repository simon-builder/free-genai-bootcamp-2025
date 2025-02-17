import pytest
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db, engine, Base

def test_get_db():
    """Test database session management"""
    db_generator = get_db()
    db = next(db_generator)
    
    try:
        # Verify we got a valid session
        assert isinstance(db, Session)
        
        # Test that we can use the session
        result = db.execute(text("SELECT 1")).scalar()  # Use text() for raw SQL
        assert result == 1
        
    finally:
        try:
            next(db_generator)  # This should trigger the finally block in get_db
        except StopIteration:
            pass

def test_engine_configuration():
    """Test engine is configured correctly"""
    assert str(engine.url) == "sqlite:///./sql_app.db"  # Test full URL
    assert engine.url.drivername == "sqlite"
    # Test that we can make a connection
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1")).scalar()
        assert result == 1

def test_base_configuration():
    """Test SQLAlchemy Base is configured"""
    assert hasattr(Base, 'metadata')
    assert Base.metadata is not None 