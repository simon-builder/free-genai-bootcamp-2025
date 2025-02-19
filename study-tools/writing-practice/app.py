import streamlit as st
from PIL import Image
from manga_ocr import MangaOcr
from openai import OpenAI
import os
from dotenv import load_dotenv
import requests
from typing import Dict, List, TypedDict, Optional, Union

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

class WordGroup(TypedDict):
    id: int
    name: str
    description: str

class Word(TypedDict):
    id: int
    kanji: str
    romaji: str
    english: str
    parts: str
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
            st.error(f"Failed to fetch groups: {str(e)}")
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
            st.error(f"Failed to fetch words for group {group_id}: {str(e)}")
            return []

@st.cache_data(ttl=300)
def fetch_groups() -> List[WordGroup]:
    """Cache groups data for 5 minutes"""
    api = LangPortalAPI()
    return api.get_groups()

@st.cache_data(ttl=300)
def fetch_words_for_groups(group_ids: List[int]) -> Dict[int, List[str]]:
    """Cache words for selected groups for 5 minutes"""
    api = LangPortalAPI()
    words_by_group = {}
    for group_id in group_ids:
        words = api.get_words_for_group(group_id)
        words_by_group[group_id] = [word['kanji'] for word in words]
    return words_by_group

def generate_sentence(selected_words: List[str]) -> Optional[Dict[str, str]]:
    """Generate a sentence using OpenAI based on selected words"""
    if not selected_words:
        return None
    
    prompt = f"""Generate a simple Japanese sentence with its English translation.
    Use one or more of these Japanese words: {', '.join(selected_words)}
    
    Requirements:
    1. The sentence should be simple and suitable for N5-N3 level
    2. Return only in this format:
    {{"en": "English sentence", "ja": "Japanese sentence"}}
    3. Use basic sentence structure (Subject + Object + Verb)
    4. The Japanese sentence must use at least one word from the provided list
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a Japanese language teacher."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        if response.choices and response.choices[0].message.content:
            result = eval(response.choices[0].message.content.strip())
            if isinstance(result, dict) and "en" in result and "ja" in result:
                return result
        
        st.error("Invalid response format from OpenAI")
        return None
    except Exception as e:
        st.error(f"Error generating sentence: {str(e)}")
        return None

@st.cache_resource
def load_ocr():
    return MangaOcr()

def main():
    st.title("Japanese Writing Practice")
    
    # Check for OpenAI API key
    if not os.getenv('OPENAI_API_KEY'):
        st.error("Please set your OpenAI API key in the .env file")
        st.stop()
    
    # Initialize session state
    if "current_sentence" not in st.session_state:
        st.session_state.current_sentence = None
    
    # Initialize all_words list
    all_words: List[str] = []
    
    # Fetch available groups
    groups = fetch_groups()
    
    # Sidebar for group selection
    st.sidebar.header("Settings")
    selected_groups = st.sidebar.multiselect(
        "Select Word Groups",
        options=[(group['id'], group['name']) for group in groups],
        format_func=lambda x: x[1]  # Display group name in dropdown
    )
    
    # Show selected word groups and their words
    if selected_groups:
        group_ids = [group_id for group_id, _ in selected_groups]
        words_by_group = fetch_words_for_groups(group_ids)
        
        st.sidebar.write("Words to practice:")
        for group_id, group_name in selected_groups:
            words = words_by_group.get(group_id, [])
            all_words.extend(words)
            st.sidebar.write(f"**{group_name}:** {', '.join(words)}")
    
    # Main app sections
    tab1, tab2 = st.tabs(["Practice", "History"])
    
    with tab1:
        st.subheader("Translation Practice")
        
        # Display practice sentence
        col1, col2 = st.columns([2, 1])
        with col1:
            if st.button("Get New Sentence"):
                if not selected_groups:
                    st.warning("Please select at least one word group")
                else:
                    with st.spinner("Generating a new sentence..."):
                        st.session_state.current_sentence = generate_sentence(all_words)
                        st.session_state.feedback = None
        
        if st.session_state.current_sentence:
            st.write("Translate this sentence to Japanese:")
            st.write(f"**{st.session_state.current_sentence['en']}**")
            
            uploaded_file = st.file_uploader(
                "Upload your handwritten answer", 
                type=["jpg", "jpeg", "png"],
                help="Take a photo of your handwritten Japanese answer"
            )
            
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption="Your handwritten answer", use_column_width=True)
                
                if st.button("Check Answer"):
                    with st.spinner("Analyzing your handwriting..."):
                        mocr = load_ocr()
                        recognized_text = mocr(image)
                        
                        correct_answer = st.session_state.current_sentence['ja']
                        is_correct = recognized_text.strip() == correct_answer.strip()
                        
                        st.write("---")
                        st.write("**Results:**")
                        st.write(f"Recognized text: {recognized_text}")
                        st.write(f"Correct answer: {correct_answer}")
                        
                        if is_correct:
                            st.success("Perfect! Your answer is correct! 🎉")
                        else:
                            st.error("Not quite right. Try again! 💪")
        else:
            st.info("Click 'Get New Sentence' to start practicing!")
    
    with tab2:
        st.subheader("Practice History")
        st.info("Practice history feature coming soon!")

if __name__ == "__main__":
    main() 