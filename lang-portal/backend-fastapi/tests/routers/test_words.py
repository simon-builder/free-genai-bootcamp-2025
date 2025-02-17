import pytest
from fastapi.testclient import TestClient

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

def test_get_words_sorting_desc(client):
    """Test descending order sorting"""
    response = client.get("/words?sort_by=kanji&order=desc")
    assert response.status_code == 200
    data = response.json()
    # Verify descending order
    assert data[0]["kanji"] > data[1]["kanji"]

def test_get_words_sorting_english(client):
    """Test sorting by english field"""
    response = client.get("/words?sort_by=english&order=asc")
    assert response.status_code == 200
    data = response.json()
    # Verify english alphabetical order
    assert data[0]["english"] <= data[1]["english"]

def test_get_words_sorting_review_stats(client):
    """Test sorting by review statistics"""
    response = client.get("/words?sort_by=correct_count&order=desc")
    assert response.status_code == 200
    data = response.json()
    # Verify correct_count is present
    assert "correct_count" in data[0]
    assert "wrong_count" in data[0]

def test_get_words_zero_limit(client):
    """Test getting all words without pagination"""
    response = client.get("/words?limit=0")
    assert response.status_code == 200
    all_words = response.json()
    
    # Get paginated results
    response = client.get("/words?limit=10")
    paginated = response.json()
    
    # Should have more or equal words when no limit
    assert len(all_words) >= len(paginated)

def test_get_words_invalid_page(client):
    """Test invalid page number"""
    response = client.get("/words?page=0")
    assert response.status_code == 200  # FastAPI converts to page 1
    
    response = client.get("/words?page=-1")
    assert response.status_code == 200  # FastAPI converts to page 1

def test_get_word_check_groups(client):
    """Test that word details include groups"""
    # Get a word ID first
    response = client.get("/words")
    words = response.json()
    word_id = words[0]["id"]
    
    # Get specific word
    response = client.get(f"/words/{word_id}")
    assert response.status_code == 200
    word = response.json()
    
    # Check group information
    assert "groups" in word
    assert isinstance(word["groups"], list)