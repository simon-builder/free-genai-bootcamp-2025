import requests
from typing import Dict, List, TypedDict
from collections import Counter

class WordGroup(TypedDict):
    id: int
    name: str
    description: str

class Word(TypedDict):
    id: int
    kanji: str
    romaji: str
    english: str
    parts: str  # We'll keep as string for now
    groups: List[WordGroup]
    type: str
    correct_count: int
    wrong_count: int

class LangPortalAPI:
    def __init__(self):
        self.base_url = "http://127.0.0.1:8000"
    
    def get_groups(self) -> List[WordGroup]:
        """Fetch all available word groups"""
        try:
            response = requests.get(f"{self.base_url}/groups")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Failed to fetch groups: {str(e)}")
            return []
    
    def get_words_for_group(self, group_id: int) -> List[Word]:
        """Fetch words for a specific group"""
        try:
            response = requests.get(
                f"{self.base_url}/groups/{group_id}",
                params={"limit": 0}  # Get all words
            )
            response.raise_for_status()
            return response.json()['words']
        except requests.RequestException as e:
            print(f"Failed to fetch words for group {group_id}: {str(e)}")
            return []

def test_api():
    api = LangPortalAPI()
    
    print("\n1. Testing GET /groups endpoint...")
    groups = api.get_groups()
    print(f"Found {len(groups)} groups:")
    for group in groups:
        print(f"- Group {group['id']}: {group['name']}")
    
    if groups:
        print("\n2. Testing GET /words for each group...")
        for group in groups:
            words = api.get_words_for_group(group['id'])
            
            # Count words by type
            type_counts = Counter(word['type'] for word in words)
            
            print(f"\nGroup {group['id']} ({group['name']}):")
            print(f"Total words: {len(words)}")
            print("Word types distribution:")
            for word_type, count in type_counts.items():
                print(f"- {word_type}: {count} words")
            
            if words:
                print("\nFirst 3 words as sample:")
                for word in words[:3]:
                    print(f"- {word['kanji']} ({word['english']}) [{word['type']}]")
            print("-" * 40)
    else:
        print("No groups found to test words endpoint")

if __name__ == "__main__":
    test_api() 