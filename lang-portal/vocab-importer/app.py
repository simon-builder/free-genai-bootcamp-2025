import streamlit as st
import json
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure OpenAI
client = OpenAI()
# client.api_key = os.getenv("OPENAI_API_KEY")


def generate_vocab_with_openai(category):
    """Generate vocabulary using OpenAI API"""
    prompt = f"""Generate a list of 5 Japanese vocabulary words for the category: {category}.
    Each word should include kanji, romaji, english translation, and parts breakdown.
    Return only the JSON array in this exact format:
    [
        {{
            "kanji": "いい",
            "romaji": "ii",
            "english": "good",
            "parts": [
                {{"kanji": "い", "romaji": ["i"]}},
                {{"kanji": "い", "romaji": ["i"]}}
            ]
        }}
    ]
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a Japanese language expert. Generate vocabulary in JSON format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        # Parse the response to ensure valid JSON
        result = json.loads(response.choices[0].message.content)
        return result
    except Exception as e:
        st.error(f"Error generating vocabulary: {str(e)}")
        return None

st.title("Vocabulary Generator")

# Input for category
category = st.text_input("Category", placeholder="Enter category name (e.g. 'adjectives', 'verbs')")

# Generate button
if st.button("Generate JSON"):
    if not category:
        st.error("Please enter a category")
    else:
        with st.spinner("Generating vocabulary..."):
            generated_data = generate_vocab_with_openai(category)
            
            if generated_data:
                # Display formatted JSON
                st.json(generated_data)
                
                # Add download button for the JSON
                json_str = json.dumps(generated_data, indent=2, ensure_ascii=False)
                st.download_button(
                    label="Download JSON",
                    file_name=f"{category}.json",
                    mime="application/json",
                    data=json_str
                )
