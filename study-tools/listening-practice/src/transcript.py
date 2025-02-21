from typing import Dict, List, Optional
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

class YouTubeTranscriptExtractor:
    @staticmethod
    def extract_video_id(url: str) -> Optional[str]:
        """Extract video ID from YouTube URL."""
        try:
            parsed_url = urlparse(url)
            
            # Handle regular YouTube URLs
            if parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
                if parsed_url.path == '/watch':
                    return parse_qs(parsed_url.query)['v'][0]
                elif parsed_url.path.startswith('/v/'):
                    return parsed_url.path.split('/')[2]
            
            # Handle youtu.be URLs
            elif parsed_url.hostname == 'youtu.be':
                return parsed_url.path[1:]
            
            return None
        except Exception:
            return None

    @staticmethod
    def get_transcript(video_id: str) -> List[Dict[str, str]]:
        """
        Get transcript for a YouTube video.
        Returns list of dictionaries with keys: text, start, duration
        """
        try:
            # Try to get English transcript first
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            
            try:
                # Try to get manual English transcript first
                transcript = transcript_list.find_manually_created_transcript(['en'])
            except:
                try:
                    # Fall back to any English transcript
                    transcript = transcript_list.find_transcript(['en'])
                except:
                    # Fall back to auto-translated English transcript
                    transcript = transcript_list.find_generated_transcript(['en'])
            
            return transcript.fetch()
            
        except Exception as e:
            raise Exception(f"Failed to get transcript: {str(e)}")

    def process_url(self, url: str) -> List[Dict[str, str]]:
        """Process YouTube URL and return transcript."""
        video_id = self.extract_video_id(url)
        if not video_id:
            raise ValueError("Invalid YouTube URL")
        
        return self.get_transcript(video_id)
