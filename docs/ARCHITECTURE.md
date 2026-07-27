# CampusAI System Architecture

## High-Level Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     Student/User                            │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│            Next.js Frontend (React + TypeScript)             │
│                                                              │
│  - Chat Interface                                            │
│  - Avatar Display                                            │
│  - Text-to-Speech                                            │
│  - Responsive UI (Tailwind CSS)                              │
└────────────────────────┬────────────────────────────────────┘
                         │ (HTTP/REST)
                         ▼
┌─────────────────────────────────────────────────────────────┐
│         FastAPI Backend (Python + Pydantic)                  │
│                                                              │
│  - Chat Endpoint (/api/chat)                                 │
│  - Query Endpoint (/api/query)                               │
│  - Health Check (/health)                                    │
│  - Authentication (Future)                                   │
└────────────────────────┬────────────────────────────────────┘
                         │
              ┌──────────┼──────────┐
              │          │          │
              ▼          ▼          ▼
        ┌──────────┐ ┌──────────┐ ┌──────────────┐
        │LangChain │ │ChromaDB  │ │Knowledge Base│
        │(RAG)     │ │(Vector DB)│ │(JSON/MD)     │
        └────┬─────┘ └──────────┘ └──────────────┘
             │
             ▼
      ┌─────────────┐
      │ Ollama Pro  │
      │ (LLM)       │
      │ (OpenAI API)│
      └─────────────┘
```

## Component Details

### Frontend (Next.js + TypeScript + Tailwind CSS)
- Renders chat interface
- Displays talking avatar
- Handles text-to-speech
- Communicates with backend via REST API

### Backend (FastAPI + Python)
- Processes incoming queries
- Manages RAG pipeline
- Coordinates with LLM
- Returns responses with citations

### Knowledge Base
- Official Centennial College information
- Stored in JSON and Markdown formats
- Indexed by ChromaDB for semantic search

### Vector Database (ChromaDB)
- Stores embeddings of knowledge base
- Enables semantic similarity search
- Retrieves relevant documents for RAG

### LLM (Ollama Pro / Local Ollama)
- Generates contextual responses
- Uses retrieved documents from RAG
- OpenAI-compatible API

## Data Flow

### Query Processing

1. **User Query** → Frontend sends query to backend
2. **Retrieval** → Backend queries ChromaDB for relevant documents
3. **Generation** → LangChain passes retrieved docs + query to LLM
4. **Response** → LLM generates response with citations
5. **Display** → Frontend displays response and plays audio

### Response Format

```json
{
  "response": "Answer text",
  "sources": [
    {
      "document": "source_name",
      "excerpt": "relevant text"
    }
  ],
  "avatar_response": "audio_url_or_text",
  "confidence": 0.95
}
```

## File Structure

```
CampusAI/
├── frontend/              # Next.js application
│   ├── app/              # Application routes
│   ├── components/       # React components
│   ├── types/            # TypeScript types
│   ├── lib/              # Utilities
│   ├── hooks/            # Custom React hooks
│   └── public/           # Static assets
│
├── backend/              # FastAPI application
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── models/       # Data models
│   │   ├── schemas/      # Pydantic schemas
│   │   ├── services/     # Business logic
│   │   └── utils/        # Utilities
│   ├── main.py           # Entry point
│   ├── config.py         # Configuration
│   └── requirements.txt   # Dependencies
│
├── knowledge/            # Knowledge base
│   ├── college_info.json
│   ├── departments/
│   ├── programs/
│   ├── facilities/
│   └── policies/
│
└── docs/                 # Documentation
    ├── ARCHITECTURE.md
    ├── API.md
    ├── SETUP.md
    └── MEETINGS.md
```

## Technology Choices

### Why Next.js?
- Built-in SSR and optimization
- Great TypeScript support
- Excellent for rapid development
- Easy deployment

### Why FastAPI?
- Fast and modern
- Automatic API documentation
- Excellent for AI/ML integration
- Easy async support

### Why LangChain?
- Abstracts LLM complexity
- Built-in RAG support
- Chain composition
- Easy to extend

### Why ChromaDB?
- Lightweight vector database
- Easy local setup
- Great for prototyping
- Semantic search support

### Why Ollama?
- Free and open-source
- Local LLM execution
- Privacy-preserving
- Easy setup and testing

## Future Scalability

The architecture is designed to be easily extended:

- **Authentication**: Add JWT middleware to FastAPI
- **Database**: Replace with PostgreSQL for user data
- **Caching**: Add Redis for response caching
- **Microservices**: Split RAG service into separate microservice
- **Monitoring**: Add logging and monitoring infrastructure
