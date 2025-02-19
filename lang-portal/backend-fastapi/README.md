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

The API documentation is automatically generated and can be accessed through:

- Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API documentation (ReDoc): `http://localhost:8000/redoc`