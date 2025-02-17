import pytest
from fastapi.testclient import TestClient

def test_get_groups(client):
    """Test getting all groups"""
    response = client.get("/groups")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    # Verify we have verb and adjective groups
    group_names = [g["name"] for g in data]
    assert "verb" in group_names
    assert "adjective" in group_names

def test_get_group_by_id(client):
    """Test getting a specific group with its words"""
    # First get a group ID
    response = client.get("/groups")
    groups = response.json()
    verb_group = next(g for g in groups if g["name"] == "verb")
    
    # Then get that specific group
    response = client.get(f"/groups/{verb_group['id']}")
    assert response.status_code == 200
    group = response.json()
    assert group["id"] == verb_group["id"]
    assert "words" in group
    assert isinstance(group["words"], list)

def test_get_group_not_found(client):
    """Test getting a non-existent group"""
    response = client.get("/groups/999999")
    assert response.status_code == 404

def test_add_word_to_group(client, db):
    """Test adding a word to a group"""
    # Get the adjective group (since we're testing with a verb)
    response = client.get("/groups")
    assert response.status_code == 200
    groups = response.json()
    adj_group = next(g for g in groups if g["name"] == "adjective")
    
    # Get a verb word
    response = client.get("/words")
    assert response.status_code == 200
    words = response.json()
    verb = next(w for w in words if "verb" in [g["name"] for g in w["groups"]])
    
    # Add verb to adjective group
    response = client.post(f"/groups/{adj_group['id']}/words/{verb['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    
    # Commit the transaction
    db.commit()
    
    # Verify word was added
    response = client.get(f"/groups/{adj_group['id']}")
    assert response.status_code == 200
    group = response.json()
    word_ids = [w["id"] for w in group["words"]]
    assert verb['id'] in word_ids

def test_add_word_to_nonexistent_group(client):
    """Test adding a word to a non-existent group"""
    response = client.post("/groups/999999/words/1")
    assert response.status_code == 404
    assert "Group not found" in response.json()["detail"]

def test_add_nonexistent_word_to_group(client):
    """Test adding a non-existent word to a group"""
    # Get a valid group ID first
    response = client.get("/groups")
    groups = response.json()
    group_id = groups[0]["id"]
    
    response = client.post(f"/groups/{group_id}/words/999999")
    assert response.status_code == 404
    assert "Word not found" in response.json()["detail"] 