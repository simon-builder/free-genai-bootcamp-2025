# Listening Practice App

A Japanese listening comprehension app that generates practice content similar to YouTube language learning test examples.

## Goal
Create an app that can analyze YouTube listening comprehension examples and generate similar practice content for Japanese language learners.

## Core Requirements
- [ ] YouTube transcript extraction using YouTube Transcript API
- [ ] Vector storage of transcripts in SQLite3
- [ ] LLM agent to analyze and generate similar content
- [ ] TTS conversion for generated content
- [ ] Simple frontend using Streamlit
- [ ] Basic guardrails for content generation
- [ ] Multiple-choice answer validation

## Optional Features
- [ ] Speech-to-Text (ASR) capabilities using OpenWhisper
- [ ] Performance tracking
- [ ] Audio replay functionality

## Technical Stack
- Database: SQLite3 with vector storage
- Frontend: Streamlit
- AI Components:
  - LLM Agent for content generation
  - TTS (Amazon Polly or alternative)
  - YouTube Transcript API
  - AI Coding Assistant (Github Copilot)

## Technical Challenges
1. Japanese language support in TTS systems
2. Vector storage implementation with SQLite3
3. YouTube transcript extraction reliability
4. Content quality guardrails

## Development Flow
1. Extract transcripts from Japanese listening comprehension videos
2. Store and analyze transcript patterns
3. Generate similar content using LLM
4. Convert generated content to speech
5. Present through Streamlit interface

## MVP Focus
- YouTube transcript extraction and analysis (focus on the first 10-15 minutes of video if it is too long)
- Basic content generation
- Simple TTS implementation
- Minimal Streamlit interface


