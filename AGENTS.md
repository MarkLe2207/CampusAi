# CampusAI - AI Development Guide

> This file provides context and rules for AI coding assistants working on the CampusAI project.

---

# Project Summary

CampusAI is an AI-powered virtual receptionist prototype for Centennial College.

The application uses Retrieval-Augmented Generation (RAG) to answer student questions using official Centennial College information.

This project is being developed for a Software Engineering Fundamentals course and may continue as a personal portfolio project after the course.

---

# Read First

Before making changes, read:

1. PROJECT_SOURCE_OF_TRUTH.md
2. TEAM_ROLES_AND_DELIVERABLES.md
3. AGENTS.md

These documents define the project architecture, scope, and team responsibilities.

---

# Tech Stack

## Frontend

- Next.js
- TypeScript
- Tailwind CSS

## Backend

- Python
- FastAPI
- Pydantic

## AI

- LangChain

## LLM

- Ollama Pro (OpenAI-Compatible API)

Development fallback:

- Local Ollama

## Vector Database

- ChromaDB

## Knowledge Base

- Markdown
- JSON

---

# Repository Structure

```
frontend/
backend/
knowledge/
docs/

PROJECT_SOURCE_OF_TRUTH.md
TEAM_ROLES_AND_DELIVERABLES.md
AGENTS.md
README.md
```

---

# Architecture

```
Student

↓

Next.js

↓

FastAPI

↓

LangChain

↓

ChromaDB

↓

Ollama Pro

↓

Response

↓

Avatar + Text-to-Speech
```

---

# Development Rules

- Follow the existing architecture.
- Keep frontend and backend separate.
- Do not introduce new frameworks unless requested.
- Keep code modular and readable.
- Reuse existing code when possible.
- Do not hardcode secrets or API keys.
- Use environment variables for configuration.

---

# Coding Style

- Use descriptive names.
- Keep functions focused.
- Avoid duplicate logic.
- Keep comments concise.
- Prioritize readability over clever implementations.

---

# Scope

Build only the agreed MVP.

Current features include:

- AI chat
- RAG
- Source citations
- Talking avatar
- Text-to-speech
- Department recommendations

Do not implement features outside the MVP unless requested.

---

# Current Progress

Completed:

- Project planning
- Technology stack finalized
- Architecture finalized
- Team responsibilities assigned

Next Steps:

- Create repository
- Backend skeleton
- Frontend skeleton
- Knowledge base
- AI integration

---

# Long-Term Vision

After the course, CampusAI may continue as a personal portfolio project.

Future versions may include:

- Multi-institution support
- Authentication
- Admin dashboard
- Analytics
- Improved AI models
- Production deployment

Design new code with extensibility in mind, but only implement the current MVP.

---

# AI Instructions

When completing a task:

- Read the relevant project documentation first.
- Stay within the current project scope.
- Preserve the agreed architecture.
- Return complete files when modifying existing code.
- Briefly explain major implementation decisions.
- Do not make unrelated changes.

If requirements are unclear, follow the PROJECT_SOURCE_OF_TRUTH.md before making assumptions.
