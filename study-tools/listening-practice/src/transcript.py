from typing import Dict, List, Optional
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

class YouTubeTranscriptExtractor:
    MAX_DURATION = 600  # 10 minutes in seconds

    @staticmethod
    def extract_video_id(url: str) -> Optional[str]:
        """Extract video ID from YouTube URL."""
        try:
            parsed_url = urlparse(url)
            
            # Handle regular YouTube URLs
            if parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
                if parsed_url.path == '/watch':
                    return parse_qs(parsed_url.query)['v'][0]
            
            # Handle youtu.be URLs
            elif parsed_url.hostname == 'youtu.be':
                return parsed_url.path[1:]
            
            return None
        except Exception:
            return None

    @staticmethod
    def get_transcript(video_id: str) -> List[Dict[str, str]]:
        """
        Get auto-generated Japanese transcript for a YouTube video (up to 10 minutes).
        Returns list of dictionaries with keys: text, start, duration
        """
        try:
            # Get list of available transcripts
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            
            # Get the auto-generated Japanese transcript directly
            transcript = transcript_list.find_generated_transcript(['ja'])
            
            # Get the full transcript
            transcript_data = transcript.fetch()
            
            # Filter transcript entries up to 10 minutes
            filtered_transcript = [
                entry for entry in transcript_data 
                if float(entry['start']) <= YouTubeTranscriptExtractor.MAX_DURATION
            ]
            
            if not filtered_transcript:
                raise Exception("No transcript entries found within the first 10 minutes")
            
            return filtered_transcript

        except Exception as e:
            raise Exception(f"Failed to get Japanese transcript: {str(e)}")

    def process_url(self, url: str) -> List[Dict[str, str]]:
        """Process YouTube URL and return Japanese transcript."""
        video_id = self.extract_video_id(url)
        if not video_id:
            raise ValueError("Invalid YouTube URL")
        
        return self.get_transcript(video_id)