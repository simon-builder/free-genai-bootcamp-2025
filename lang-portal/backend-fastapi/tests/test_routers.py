from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
import pytest

# Words Router Tests
def test_get_words(client):
    response = client.get("/words")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    
    # Debug: Print all words
    print("\nAvailable words:")
    for word in data:
        print(f"kanji: {word['kanji']}, english: {word['english']}")
    
    # Find あげる in the response
    ageru = next(word for word in data if word["kanji"] == "あげる")
    assert ageru["english"] == "to give"

def test_get_words_pagination(client):
    # Test with different page sizes
    response = client.get("/words?page=1&limit=5")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 5  # Should return exactly 5 items

def test_get_words_sorting(client):
    # Test sorting by different fields
    response = client.get("/words?sort_by=kanji&order=asc")
    data = response.json()
    # Japanese あ comes before い in sorting
    assert data[0]["kanji"] == "あげる"

def test_get_word_by_id(client):
    # First get a word ID from the list
    response = client.get("/words")
    words = response.json()
    word_id = words[0]["id"]

    # Then get that specific word
    response = client.get(f"/words/{word_id}")
    assert response.status_code == 200
    word = response.json()
    assert word["id"] == word_id

def test_get_word_not_found(client):
    response = client.get("/words/999999")  # Non-existent ID
    assert response.status_code == 404