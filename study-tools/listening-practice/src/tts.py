from pathlib import Path
from openai import OpenAI
import os
import hashlib

class TTSGenerator:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.model = "tts-1"
        self.voices = {
            "female": "nova",
            "male": "onyx"
        }
        self.audio_dir = Path("audio_cache")
        
        # Create directories if they don't exist
        self.audio_dir.mkdir(exist_ok=True)
    
    def _get_cache_path(self, text: str) -> Path:
        """Generate a unique filename based on the text content."""
        text_hash = hashlib.md5(text.encode()).hexdigest()
        return self.audio_dir / f"{text_hash}.mp3"
    
    def _split_conversation(self, conversation: str) -> list:
        """Split conversation into segments with speaker identification."""
        lines = conversation.split('\n')
        segments = []
        
        # Gender indicators
        male_indicators = ["男性", "MAN", "MALE", "男", "くん", "君", "さん（男性）"]
        female_indicators = ["女性", "WOMAN", "FEMALE", "女", "ちゃん", "さん（女性）"]
        
        # Keep track of speakers and their genders
        speakers = {}
        last_voice = None
        
        for line in lines:
            if ':' in line:
                speaker, text = line.split(':', 1)
                speaker = speaker.strip()
                
                # Check if speaker has specific gender indicators
                speaker_upper = speaker.upper()
                is_male = any(indicator in speaker_upper for indicator in male_indicators)
                is_female = any(indicator in speaker_upper for indicator in female_indicators)
                
                # If speaker not seen before, assign voice
                if speaker not in speakers:
                    if is_male:
                        voice_type = "male"
                    elif is_female:
                        voice_type = "female"
                    else:
                        # No specific gender indicator, alternate voices
                        voice_type = "male" if last_voice == "female" else "female"
                    speakers[speaker] = voice_type
                
                last_voice = speakers[speaker]
                segments.append({
                    "text": text.strip(),
                    "voice": self.voices[speakers[speaker]]
                })
        
        return segments
    
    def generate_conversation_audio(self, conversation: str) -> str:
        """Generate audio for entire conversation with alternating voices."""
        cache_path = self._get_cache_path(conversation)
        
        # Return cached file if it exists
        if cache_path.exists():
            return str(cache_path)
        
        try:
            # Split conversation and generate audio
            segments = self._split_conversation(conversation)
            
            # Generate audio for the first segment
            response = self.client.audio.speech.create(
                model=self.model,
                voice=segments[0]["voice"],
                input=segments[0]["text"]
            )
            response.stream_to_file(str(cache_path))
            
            # Generate and append audio for remaining segments
            for segment in segments[1:]:
                response = self.client.audio.speech.create(
                    model=self.model,
                    voice=segment["voice"],
                    input=segment["text"]
                )
                response.stream_to_file(str(cache_path))
            
            return str(cache_path)
            
        except Exception as e:
            raise Exception(f"Failed to generate audio: {str(e)}") 