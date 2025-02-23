from typing import Dict, List, TypedDict
from openai import OpenAI
import json

class GeneratedContent(TypedDict):
    context: str
    conversation: str
    question: str
    options: List[str]
    correct_answer: str
    explanation: str

class LLMGenerator:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4o-mini"
        
    def _clean_json_response(self, content: str) -> str:
        """Clean JSON string from markdown formatting."""
        # Remove markdown code block if present
        if content.startswith('```'):
            # Remove first line (```json)
            content = content.split('\n', 1)[1]
            # Remove last line (```)
            content = content.rsplit('\n', 1)[0]
        return content.strip()
        
    def analyze_transcript(self, transcript: List[Dict[str, str]]) -> Dict[str, str]:
        """Analyze transcript to understand theme and style."""
        transcript_text = "\n".join([entry["text"] for entry in transcript])
        
        messages = [
            {
                "role": "system",
                "content": "You are a Japanese language expert. Always respond in JSON format."
            },
            {
                "role": "user",
                "content": f"""
                Analyze this Japanese transcript and provide the following in JSON format:
                {{
                    "theme": "main theme or situation",
                    "style": "conversation style (casual/formal)",
                    "level": "language difficulty level"
                }}
                
                Transcript:
                {transcript_text}
                """
            }
        ]
        
        response = self.client.chat.completions.create(
            messages=messages,
            model=self.model
        )
        
        try:
            # Get the response content and clean it
            content = self._clean_json_response(response.choices[0].message.content)
            # Parse JSON from the response
            return json.loads(content)
        except json.JSONDecodeError as e:
            print(f"JSON Parse Error: {content}")
            raise Exception("Failed to parse analysis response")

    def generate_practice(self, analysis: Dict[str, str]) -> GeneratedContent:
        """Generate new conversation and question based on analysis."""
        messages = [
            {
                "role": "system",
                "content": """You are a Japanese language expert creating listening practice materials.
                Always respond in JSON format. Make sure to vary the correct answer between A, B, C, and D.
                The correct answer should logically follow from the conversation and not always be A."""
            },
            {
                "role": "user",
                "content": f"""
                Create a listening practice based on this analysis:
                Theme: {analysis.get('theme')}
                Style: {analysis.get('style')}
                Level: {analysis.get('level')}
                
                Create a natural conversation and a question where the correct answer could be any option (A, B, C, or D).
                
                Respond with ONLY a JSON object in this exact format:
                {{
                    "context": "brief situation introduction in Japanese",
                    "conversation": "a new natural conversation between two people in Japanese",
                    "question": "a question about the conversation in Japanese",
                    "options": ["option A in Japanese", "option B in Japanese", "option C in Japanese", "option D in Japanese"],
                    "correct_answer": "A, B, C, or D (randomly chosen)",
                    "explanation": "brief explanation in English why this answer is correct"
                }}
                
                Important: The correct_answer should be randomly chosen among A, B, C, or D, not always A.
                """
            }
        ]
        
        response = self.client.chat.completions.create(
            messages=messages,
            model=self.model
        )
        
        try:
            # Get the response content and clean it
            content = self._clean_json_response(response.choices[0].message.content)
            # Parse JSON from the response
            return json.loads(content)
        except json.JSONDecodeError as e:
            print(f"JSON Parse Error: {content}")
            raise Exception("Failed to parse practice generation response") 