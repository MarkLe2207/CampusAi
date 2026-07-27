# CampusAI – Project Source of Truth

> **Version:** 1.0  
> **Course:** Software Engineering Fundamentals  
> **Institution:** Centennial College  
> **Project Lead:** Abrar Habib

---

# 1. Project Overview

CampusAI is an AI-powered virtual receptionist designed for Centennial College students. It provides quick, conversational answers to common questions using Retrieval-Augmented Generation (RAG) over official college information.

The goal is to demonstrate software engineering principles, AI integration, teamwork, and modern web development through a functional prototype.

---

# 2. Objectives

- Help students find information faster.
- Reduce repetitive questions to staff.
- Demonstrate AI + RAG integration.
- Build a maintainable full-stack application.
- Follow an organized software engineering workflow.

---

# 3. Minimum Viable Product (MVP)

The prototype will support:

- AI chat interface
- RAG using official Centennial College information
- Source citations
- Talking avatar
- Text-to-speech responses
- Department recommendations when appropriate

---

# 4. Out of Scope

The following are **not** part of the course project:

- Student authentication
- Database accounts
- Live student records
- Course registration
- Payment processing
- Email integration
- Mobile application
- Production deployment

---

# 5. Technology Stack

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

## Avatar

- TalkingHead

## Speech

- Browser Speech API

## Version Control

- Git + GitHub

## Project Management

- Trello

---

# 6. High-Level Architecture

```
Student
      │
      ▼
 Next.js Frontend
      │
      ▼
 FastAPI Backend
      │
      ▼
 LangChain
      │
      ▼
 ChromaDB
      │
      ▼
 Ollama Pro
      │
      ▼
 AI Response
      │
      ├── Source Citation
      ├── Talking Avatar
      └── Text-to-Speech
```

---

# 7. Repository Structure

```
CampusAI/

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

# 8. Development Workflow

1. Plan feature
2. Create Trello task
3. Implement
4. Test
5. Review
6. Merge into main

---

# 9. Coding Standards

- Keep code simple and readable.
- Use meaningful names.
- Separate frontend and backend responsibilities.
- Avoid duplicate code.
- Comment only when necessary.
- Use environment variables for secrets.
- Keep modules small and focused.

---

# 10. Team Workflow

- Scrum methodology
- Weekly meetings
- GitHub for version control
- Trello for task tracking
- Feature branches when possible
- Regular progress updates

---

# 11. Current Milestones

## Meeting 1

- Project approved
- Scope finalized
- Tech stack finalized
- Team roles assigned

## Meeting 2

- Repository setup
- Architecture review
- Backend skeleton
- Frontend skeleton

## Meeting 3

- Core AI integration
- Knowledge base integration

## Meeting 4

- Integration
- Testing
- Bug fixes

## Meeting 5

- Final presentation
- Demonstration
- Submission

---

# 12. Long-Term Vision (Post-Course)

After the course, CampusAI will continue as a personal portfolio project.

Potential future improvements include:

- Support for multiple colleges and universities
- User authentication
- Admin dashboard
- Voice conversations
- Analytics
- Better avatars
- Production deployment
- Improved AI models
- More scalable knowledge management

The course version is intentionally modular so these features can be added without major architectural changes.

---

# 13. Important Decisions

- Centennial College is the initial institution.
- Ollama Pro is the primary LLM provider.
- Local Ollama may be used during development.
- ChromaDB will store document embeddings.
- Official college information will be used as the knowledge base.
- This project is a prototype intended for demonstration purposes.

---

# 14. Definition of Done

A task is considered complete when:

- Requirements are implemented.
- Code runs without errors.
- Basic testing has been completed.
- Documentation is updated if needed.
- Changes are committed to GitHub.
- The feature is ready to demonstrate.

---

# 15. Guiding Principles

- Build only what the MVP requires.
- Keep the architecture simple.
- Prioritize readability over complexity.
- Make decisions the team can understand.
- Write code that can be extended after the course.
