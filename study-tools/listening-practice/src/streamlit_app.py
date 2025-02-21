import streamlit as st
from transcript import YouTubeTranscriptExtractor

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

    # Header
    st.title("🎧 Listening Practice Generator")
    st.markdown("""
    Create listening practice exercises from YouTube videos.
    Enter a YouTube URL below to get started.
    """)

    # Initialize YouTube transcript extractor
    transcript_extractor = YouTubeTranscriptExtractor()

    # Input section
    with st.container():
        youtube_url = st.text_input(
            "YouTube URL",
            placeholder="https://www.youtube.com/watch?v=..."
        )

        if st.button("Generate Practice", type="primary"):
            if youtube_url:
                try:
                    with st.spinner("Fetching transcript..."):
                        transcript = transcript_extractor.process_url(youtube_url)
                        display_transcript(transcript)
                except ValueError as e:
                    st.error(f"Error: {str(e)}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
            else:
                st.warning("Please enter a YouTube URL")

    # About section
    with st.sidebar:
        st.header("About")
        st.markdown("""
        This app helps create listening practice exercises from YouTube videos.
        
        **Features**:
        - ✅ Transcript extraction
        - 🔜 Question generation
        - 🔜 Audio segments
        """)

if __name__ == "__main__":
    main()
