import pytest
from fastapi.testclient import TestClient

def test_create_study_session(client, db):
    """Test creating a new study session"""
    # Get a group first
    response = client.get("/groups")
    assert response.status_code == 200
    groups = response.json()
    group_id = groups[0]["id"]
    
    # Create session data
    session_data = {
        "group_id": group_id,
        "study_activity_id": 1,  # From seed data
        "start_time": "2024-03-15T10:00:00"
    }
    
    # Create study session
    response = client.post("/study_sessions", json=session_data)
    assert response.status_code == 200
    session = response.json()
    assert session["group_id"] == group_id
    assert session["study_activity_id"] == 1

def test_create_study_session_invalid_group(client):
    """Test creating session with non-existent group"""
    session_data = {
        "group_id": 999999,
        "study_activity_id": 1,
        "start_time": "2024-03-15T10:00:00"
    }
    
    response = client.post("/study_sessions", json=session_data)
    assert response.status_code == 404
    assert "Group not found" in response.json()["detail"]

def test_create_word_review(client, db):
    """Test adding a word review to a session"""
    # First create a session
    response = client.get("/groups")
    groups = response.json()
    group_id = groups[0]["id"]
    
    session_data = {
        "group_id": group_id,
        "study_activity_id": 1,
        "start_time": "2024-03-15T10:00:00"
    }
    
    response = client.post("/study_sessions", json=session_data)
    assert response.status_code == 200
    session = response.json()
    
    # Get a word from the group
    response = client.get(f"/groups/{group_id}")
    assert response.status_code == 200
    group = response.json()
    word_id = group["words"][0]["id"]
    
    # Create review
    review_data = {
        "word_id": word_id,
        "correct": True
    }
    
    response = client.post(f"/study_sessions/{session['id']}/review", json=review_data)
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_create_review_invalid_session(client):
    """Test adding review to non-existent session"""
    review_data = {
        "word_id": 1,
        "correct": True
    }
    
    response = client.post("/study_sessions/999999/review", json=review_data)
    assert response.status_code == 404
    assert "Study session not found" in response.json()["detail"] 