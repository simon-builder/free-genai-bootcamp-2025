import streamlit as st
from transcript import YouTubeTranscriptExtractor
from db import Database

def display_transcript(transcript):
    """Display transcript in a readable format."""
    st.subheader("Transcript")
    for entry in transcript:
        timestamp = f"{int(entry['start'] // 60)}:{int(entry['start'] % 60):02d}"
        st.text(f"{timestamp} - {entry['text']}")

def main():
    # Set page config
    st.set_page_config(
        page_title="Listening Practice App",
        page_icon="🎧",
        layout="wide"
    )

    # Initialize components
    transcript_extractor = YouTubeTranscriptExtractor()
    db = Database()

    # Header
    st.title("🎧 Listening Practice Generator")
    st.markdown("""
    Create listening practice exercises from YouTube videos.
    Enter a YouTube URL below to get started.
    """)

    # Input section
    youtube_url = st.text_input(
        "YouTube URL",
        placeholder="https://www.youtube.com/watch?v=..."
    )

    if st.button("Generate Practice", type="primary"):
        if not youtube_url:
            st.warning("Please enter a YouTube URL")
            return

        try:
            video_id = transcript_extractor.extract_video_id(youtube_url)
            if not video_id:
                st.error("Invalid YouTube URL")
                return

            with st.spinner("Fetching transcript..."):
                transcript = transcript_extractor.process_url(youtube_url)
                
                # Save to database
                db.save_video(video_id, youtube_url)
                db.save_transcript(video_id, transcript)
                
                display_transcript(transcript)

        except Exception as e:
            st.error(f"Failed to process video: {str(e)}")

    # About section
    with st.sidebar:
        st.header("About")
        st.markdown("""
        This app helps create listening practice exercises from YouTube videos.
        
        **Features**:
        - ✅ Japanese transcript extraction
        - ✅ Database storage
        - 🔜 Question generation
        - 🔜 Audio segments
        """)

if __name__ == "__main__":
    main()
