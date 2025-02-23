import streamlit as st
import os
from transcript import YouTubeTranscriptExtractor
from db import Database
from llm import LLMGenerator
from dotenv import load_dotenv
from tts import TTSGenerator

# Load environment variables
load_dotenv()

def display_generated_content():
    """Display generated listening practice content."""
    content = st.session_state.generated_content
    
    st.subheader("Generated Listening Practice")
    
    # Display context
    st.write("Context:")
    st.write(content['context'])
    
    # Display conversation with audio
    st.write("Conversation:")
    
    # Generate new audio for each new content
    tts = TTSGenerator(os.getenv('OPENAI_API_KEY'))
    try:
        audio_path = tts.generate_conversation_audio(content['conversation'])
        st.audio(audio_path)
    except Exception as e:
        st.error(f"Failed to generate audio: {str(e)}")
    
    # Display conversation text
    st.write(content['conversation'])
    
    # Display question section
    st.write("Question:")
    st.write(content['question'])
    
    # Display options and get user selection
    selected_answer = st.radio(
        "Choose your answer:",
        options=['A', 'B', 'C', 'D'],
        key='answer_radio'
    )
    
    # Display options
    for i, option in enumerate(['A', 'B', 'C', 'D']):
        st.write(f"{option}: {content['options'][i]}")
    
    # Check answer button
    if st.button("Check Answer", key='check_button'):
        if selected_answer == content['correct_answer']:
            st.success("Correct! 🎉")
        else:
            st.error(f"Incorrect. The correct answer is {content['correct_answer']}")
        st.info(f"Explanation: {content['explanation']}")

def main():
    # Set page config
    st.set_page_config(
        page_title="Listening Practice Generator",
        page_icon="🎧",
        layout="wide"
    )

    # Initialize session state
    if 'generated_content' not in st.session_state:
        st.session_state.generated_content = None

    # Initialize components
    transcript_extractor = YouTubeTranscriptExtractor()
    db = Database()
    llm_generator = LLMGenerator(os.getenv('OPENAI_API_KEY'))

    # Header
    st.title("🎧 Listening Practice Generator")
    st.markdown("""
    Create listening practice exercises from YouTube videos.
    Enter a YouTube URL below to get started.
    """)

    # Input section
    youtube_url = st.text_input(
        "YouTube URL",
        placeholder="https://www.youtube.com/watch?v=...",
        key='url_input'
    )

    if st.button("Generate Practice", type="primary"):
        if not youtube_url:
            st.warning("Please enter a YouTube URL")
            return

        try:
            # Process video and get transcript
            video_id = transcript_extractor.extract_video_id(youtube_url)
            if not video_id:
                st.error("Invalid YouTube URL")
                return

            with st.spinner("Generating listening practice..."):
                # Get transcript
                transcript = transcript_extractor.process_url(youtube_url)
                
                # Save to database
                db.save_video(video_id, youtube_url)
                db.save_transcript(video_id, transcript)
                
                # Generate practice content
                analysis = llm_generator.analyze_transcript(transcript)
                generated_content = llm_generator.generate_practice(analysis)
                
                # Save generated content
                db.save_generated_content(video_id, generated_content)
                
                # Reset audio state for new content
                if 'audio_path' in st.session_state:
                    del st.session_state.audio_path
                if 'content_id' in st.session_state:
                    del st.session_state.content_id
                
                # Store in session state
                st.session_state.generated_content = generated_content

        except Exception as e:
            st.error(f"Failed to process video: {str(e)}")

    # Display content if available
    if st.session_state.generated_content:
        display_generated_content()

    # About section
    with st.sidebar:
        st.header("About")
        st.markdown("""
        This app helps create listening practice exercises from YouTube videos.
        
        **Features**:
        - ✅ Japanese transcript extraction
        - ✅ Database storage
        - ✅ AI-generated practice
        - ✅ Interactive questions
        """)

if __name__ == "__main__":
    main()
