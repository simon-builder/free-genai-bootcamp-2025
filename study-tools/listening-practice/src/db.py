import sqlite3
from typing import Dict, List, Optional
from datetime import datetime

class Database:
    def __init__(self, db_path: str = "listening_practice.db"):
        self.db_path = db_path
        self.init_db()

    def get_connection(self):
        """Create a database connection."""
        return sqlite3.connect(self.db_path)

    def init_db(self):
        """Initialize the database with required tables."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Create videos table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS videos (
                    video_id TEXT PRIMARY KEY,
                    url TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create transcripts table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS transcripts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    video_id TEXT NOT NULL,
                    text TEXT NOT NULL,
                    start_time FLOAT NOT NULL,
                    duration FLOAT NOT NULL,
                    FOREIGN KEY (video_id) REFERENCES videos (video_id)
                )
            ''')
            
            # Create generated_content table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS generated_content (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    video_id TEXT NOT NULL,
                    context TEXT NOT NULL,
                    conversation TEXT NOT NULL,
                    question TEXT NOT NULL,
                    options TEXT NOT NULL,
                    correct_answer TEXT NOT NULL,
                    explanation TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (video_id) REFERENCES videos (video_id)
                )
            ''')
            
            conn.commit()

    def save_video(self, video_id: str, url: str) -> bool:
        """Save video information to database."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT OR REPLACE INTO videos (video_id, url) VALUES (?, ?)",
                    (video_id, url)
                )
                conn.commit()
                return True
        except Exception as e:
            print(f"Error saving video: {e}")
            return False

    def save_transcript(self, video_id: str, transcript: List[Dict]) -> bool:
        """Save transcript entries to database."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                
                # Clear existing transcript entries for this video
                cursor.execute("DELETE FROM transcripts WHERE video_id = ?", (video_id,))
                
                # Insert all transcript entries
                cursor.executemany(
                    """
                    INSERT INTO transcripts (video_id, text, start_time, duration)
                    VALUES (?, ?, ?, ?)
                    """,
                    [(video_id, entry['text'], entry['start'], entry['duration'])
                     for entry in transcript]
                )
                
                conn.commit()
                return True
        except Exception as e:
            print(f"Error saving transcript: {e}")
            return False

    def get_video_transcript(self, video_id: str) -> Optional[List[Dict]]:
        """Retrieve transcript for a video."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    SELECT text, start_time, duration
                    FROM transcripts
                    WHERE video_id = ?
                    ORDER BY start_time
                    """,
                    (video_id,)
                )
                
                results = cursor.fetchall()
                if results:
                    return [
                        {
                            'text': text,
                            'start': start_time,
                            'duration': duration
                        }
                        for text, start_time, duration in results
                    ]
                return None
        except Exception as e:
            print(f"Error retrieving transcript: {e}")
            return None

    def video_exists(self, video_id: str) -> bool:
        """Check if a video exists in the database."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT 1 FROM videos WHERE video_id = ?",
                (video_id,)
            )
            return cursor.fetchone() is not None

    def save_generated_content(self, video_id: str, content: Dict) -> bool:
        """Save generated practice content to database."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    INSERT INTO generated_content 
                    (video_id, context, conversation, question, options, correct_answer, explanation)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        video_id,
                        content['context'],
                        content['conversation'],
                        content['question'],
                        str(content['options']),  # Convert list to string
                        content['correct_answer'],
                        content['explanation']
                    )
                )
                conn.commit()
                return True
        except Exception as e:
            print(f"Error saving generated content: {e}")
            return False

    def get_generated_content(self, video_id: str) -> Optional[List[Dict]]:
        """Retrieve all generated content for a video."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    SELECT context, conversation, question, options, correct_answer, explanation
                    FROM generated_content
                    WHERE video_id = ?
                    ORDER BY created_at DESC
                    """,
                    (video_id,)
                )
                
                results = cursor.fetchall()
                if results:
                    return [{
                        'context': row[0],
                        'conversation': row[1],
                        'question': row[2],
                        'options': eval(row[3]),  # Convert string back to list
                        'correct_answer': row[4],
                        'explanation': row[5]
                    } for row in results]
                return None
        except Exception as e:
            print(f"Error retrieving generated content: {e}")
            return None
