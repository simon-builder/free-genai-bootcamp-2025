# Listening Practice App

An optional app focused on improving Japanese listening comprehension through AI-generated conversations and comprehension questions.

## Goal
Enable users to practice listening comprehension through generated conversations with context and verify understanding through multiple-choice questions.

## Acceptance Criteria
- [ ] System generates contextual introduction for each conversation scenario
- [ ] Creates dialogue (N5-N3 level) between two speakers in Japanese
- [ ] Converts dialogue to speech using TTS model
- [ ] Generates 1 relevant comprehension question based on the conversation
- [ ] Provides 4 multiple-choice answers for the question

## Constraints
- Limited to Japanese language only
- Conversations should be short (around 30 seconds)
- Vocabulary limited to common expressions (N5-N3 level)

## Technical Components
- TTS Model integration
- Conversation generation using LLM
- Question generation system
- Answer validation and scoring

## Example Flow
1. User starts new practice session
2. System presents situation context: "At a restaurant ordering food"
3. Plays generated conversation between customer and waiter
4. Presents question: "What did the customer order?"
5. Shows 4 multiple-choice options
6. Provides feedback on user's answer

## Personal Learning Goals
- Implement TTS models
- Design natural conversation flows
- Create meaningful comprehension question
- Handle audio processing in web applications


