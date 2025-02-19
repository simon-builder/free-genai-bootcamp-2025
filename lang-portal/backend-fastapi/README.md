# Backend Project Structure

The backend is built using FastAPI and follows a modular structure for better organization and maintainability.

## Project Structure

app/
├── main.py # FastAPI application entry point
├── database.py # Database connection and session management
├── models/ # SQLAlchemy models (database tables)
│ ├── init.py
│ ├── word.py # Word entity model
│ ├── group.py # Word group/category model
│ ├── study_activity.py # Learning activity tracking
│ ├── study_session.py # Study session management
│ └── word_review_item.py # Individual word review records
├── schemas/ # Pydantic models for API validation
│ ├── init.py
│ ├── word.py # Word-related schemas
│ ├── group.py # Group-related schemas
│ ├── study_session.py # Study session schemas
│ └── word_review.py # Word review schemas
└── routers/ # API endpoints organization
├── init.py
├── words.py # Word-related endpoints
├── groups.py # Group management endpoints
└── study_sessions.py # Study session endpoints


## API Documentation

Available endpoints:
- Words
  - `GET /words` - Get list of words with pagination and sorting
  - `GET /words/{word_id}` - Get specific word details
- Groups
  - `GET /groups` - Get all groups
  - `GET /groups/{group_id}` - Get specific group details
  - `POST /groups/{group_id}/words/{word_id}` - Add word to group
- Study Sessions
  - `POST /study_sessions` - Create new study session
  - `POST /study_sessions/{session_id}/review` - Submit word review in session

For the most up-to-date and detailed documentation of all implemented endpoints, please refer to the Swagger UI documentation at `http://localhost:8000/docs`.