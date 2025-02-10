Suggested project structure

app/
├── main.py              # FastAPI application entry point
├── database.py          # Database connection and session management
├── models/             # SQLAlchemy models
│   ├── __init__.py
│   ├── word.py
│   ├── group.py
│   ├── study_activity.py
│   ├── study_session.py
│   └── word_review_item.py
├── schemas/            # Pydantic models for request/response
│   ├── __init__.py
│   ├── word.py
│   ├── group.py
│   ├── study_session.py
│   └── word_review.py
└── routers/           # API route handlers
    ├── __init__.py
    ├── words.py
    ├── groups.py
    └── study_sessions.py