import streamlit as st
from PIL import Image
from manga_ocr import MangaOcr

# Dummy data
DUMMY_WORD_GROUPS = {
    "Verbs": ["食べる", "飲む", "行く", "見る", "読む"],
    "Adjectives": ["大きい", "小さい", "良い", "悪い", "暑い"],
    "Nouns": ["猫", "犬", "本", "車", "家"],
    "Particles": ["は", "が", "を", "に", "で"]
}

DUMMY_SENTENCES = [
    {"en": "The cat drinks milk", "ja": "猫が牛乳を飲む"},
    {"en": "I read a book", "ja": "私は本を読む"},
    {"en": "The dog is big", "ja": "犬は大きい"},
]

# Initialize MangaOCR
@st.cache_resource
def load_ocr():
    return MangaOcr()

def get_random_sentence():
    import random
    return random.choice(DUMMY_SENTENCES)

def main():
    st.title("Japanese Writing Practice")
    
    # Initialize session state for tracking current sentence
    if "current_sentence" not in st.session_state:
        st.session_state.current_sentence = None
    
    # Sidebar for word group selection
    st.sidebar.header("Settings")
    word_groups = st.sidebar.multiselect(
        "Select Word Groups",
        list(DUMMY_WORD_GROUPS.keys()),
        default=["Verbs", "Nouns"]
    )
    
    # Show selected word groups
    if word_groups:
        st.sidebar.write("Words to practice:")
        for group in word_groups:
            st.sidebar.write(f"**{group}:** {', '.join(DUMMY_WORD_GROUPS[group])}")
    
    # Main app sections
    tab1, tab2 = st.tabs(["Practice", "History"])
    
    with tab1:
        st.subheader("Translation Practice")
        
        # Display practice sentence
        col1, col2 = st.columns([2, 1])
        with col1:
            if st.button("Get New Sentence"):
                st.session_state.current_sentence = get_random_sentence()
                st.session_state.feedback = None
        
        if st.session_state.current_sentence:
            st.write("Translate this sentence to Japanese:")
            st.write(f"**{st.session_state.current_sentence['en']}**")
            
            # Image upload
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
                        
                        # Simple comparison (we can make this more sophisticated later)
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