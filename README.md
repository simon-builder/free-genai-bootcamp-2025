# Language Learning Platform

Supertype3 core repository containing language learning applications and tools.

## Project Structure

```
.
├── lang-portal/               # Main application
│   ├── backend-fastapi/      # REST API for vocabulary and study management
│   ├── frontend-next/        # Next.js web interface
│   └── vocab-importer/       # Tool for importing vocabulary data
│
├── study-tools/              # Standalone learning applications
│   └── writing-practice/     # Japanese handwriting practice with OCR
│
├── sentence-constructor/     # AI prompt engineering exercise for language learning
│
└── genai-architecture/       # AI integration planning and requirements
```

## Tech Stack
- Backend: FastAPI, SQLAlchemy, SQLite
- Frontend: Next.js, TypeScript, Tailwind CSS
- AI Tools: OpenAI API, MangaOCR