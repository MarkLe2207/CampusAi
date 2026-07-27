# CampusAI - AI-Powered Virtual Receptionist

> An intelligent campus assistant platform for Centennial College students powered by AI and Retrieval-Augmented Generation (RAG).

## Project Overview

CampusAI is a prototype AI application designed to help Centennial College students find information quickly through a conversational interface. The system uses official college information indexed in a vector database to provide accurate, sourced answers to common student questions.

**Course**: Software Engineering Fundamentals  
**Institution**: Centennial College  
**Project Lead**: Abrar Habib

## Features

### MVP (Minimum Viable Product)

- 💬 **AI Chat Interface** - Conversational Q&A with students
- 🔍 **Retrieval-Augmented Generation (RAG)** - Answers based on official college information
- 📚 **Source Citations** - Displays where information comes from
- 🎬 **Talking Avatar** - Visual avatar for responses
- 🔊 **Text-to-Speech** - Audio output of responses
- 🏢 **Department Recommendations** - Suggests relevant departments

### Out of Scope (Not in Current Version)

- Student authentication or login
- Database student records
- Course registration
- Payment processing
- Email integration
- Mobile application
- Production deployment

## Technology Stack

### Frontend
- **Next.js 14+** - React framework with server-side rendering
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework

### Backend
- **Python 3.11+** - Server-side language
- **FastAPI** - Modern, fast web framework
- **Pydantic** - Data validation

### AI/ML
- **LangChain** - LLM framework and RAG orchestration
- **ChromaDB** - Vector database for embeddings
- **Ollama Pro** - Local LLM with OpenAI-compatible API
- **Sentence Transformers** - Embedding generation

### Infrastructure
- **Git + GitHub** - Version control
- **Docker** - Containerization (optional)

## Project Structure

```
CampusAI/
├── frontend/                    # Next.js web application
│   ├── app/                     # Application routes (Next.js App Router)
│   ├── components/              # Reusable React components
│   ├── types/                   # TypeScript type definitions
│   ├── lib/                     # Utility functions
│   ├── hooks/                   # Custom React hooks
│   ├── public/                  # Static assets
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.ts
│   └── next.config.js
│
├── backend/                     # FastAPI application
│   ├── app/
│   │   ├── api/                 # API route handlers
│   │   ├── models/              # Data models
│   │   ├── schemas/             # Pydantic validation schemas
│   │   ├── services/            # Business logic
│   │   └── utils/               # Helper functions
│   ├── main.py                  # Application entry point
│   ├── config.py                # Configuration management
│   ├── requirements.txt          # Python dependencies
│   └── .env.example
│
├── knowledge/                   # Knowledge base for RAG
│   ├── college_info.json        # General college information
│   ├── departments/             # Department information
│   ├── programs/                # Program information
│   ├── facilities/              # Campus facilities
│   └── policies/                # College policies
│
├── docs/                        # Project documentation
│   ├── SETUP.md                 # Development setup guide
│   ├── ARCHITECTURE.md          # System architecture
│   ├── API.md                   # API documentation
│   └── MEETINGS.md              # Meeting notes
│
├── PROJECT_SOURCE_OF_TRUTH.md   # Project vision & decisions
├── TEAM_ROLES_AND_DELIVERABLES.md  # Team responsibilities
├── AGENTS.md                    # AI coding guidelines
├── README.md                    # This file
├── .gitignore
└── CHANGELOG.md
```

## Quick Start

### Prerequisites

- Node.js 18+ and npm
- Python 3.11+
- Git
- Ollama (for local LLM, optional during development)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/campusai.git
cd campusai
```

2. **Frontend Setup**
```bash
cd frontend
npm install
npm run dev
```

Frontend will be available at `http://localhost:3000`

3. **Backend Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Backend will be available at `http://localhost:8000`

4. **Ollama Setup** (Optional - for local LLM)
```bash
# Download from https://ollama.ai
ollama pull mistral
```

For detailed setup instructions, see [SETUP.md](docs/SETUP.md).

## API Documentation

Once the backend is running, visit `http://localhost:8000/docs` for interactive API documentation.

### Key Endpoints

- `GET /` - Health check
- `GET /health` - Status
- `POST /api/query` - Submit a query to the AI

See [API.md](docs/API.md) for complete documentation.

## Architecture

```
Student Input
    ↓
Next.js Frontend (Chat UI)
    ↓ (HTTP/REST)
FastAPI Backend
    ↓
LangChain RAG Pipeline
    ├─→ ChromaDB (Vector Search)
    ├─→ Knowledge Base (Documents)
    └─→ Ollama/LLM (Response Generation)
    ↓
Response with Citations
    ↓
Avatar + Text-to-Speech
    ↓
Student Output
```

For detailed architecture information, see [ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Development Workflow

1. Create a feature branch: `git checkout -b feature/feature-name`
2. Make your changes following coding standards
3. Test your changes locally
4. Commit with clear messages: `git commit -m "feat: add feature"`
5. Push to remote: `git push origin feature/feature-name`
6. Create a pull request for review

## Project Documents

- **[PROJECT_SOURCE_OF_TRUTH.md](PROJECT_SOURCE_OF_TRUTH.md)** - Project vision, objectives, and technical decisions
- **[TEAM_ROLES_AND_DELIVERABLES.md](TEAM_ROLES_AND_DELIVERABLES.md)** - Team structure and responsibilities
- **[AGENTS.md](AGENTS.md)** - Coding guidelines and AI assistant instructions
- **[docs/SETUP.md](docs/SETUP.md)** - Development environment setup
- **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)** - System architecture and design
- **[docs/API.md](docs/API.md)** - API documentation (to be created)

## Team

| Role | Team Member | Responsibilities |
|------|------------|-----------------|
| Project Lead / Scrum Master | Abrar Habib | Project coordination, backend, LangChain integration |
| AI Research Lead | Mathew | Knowledge base curation, RAG setup |
| UI/UX Lead | Syed | Frontend development, user interface |
| Documentation Lead | Mark | Project documentation, requirements |
| QA & Presentation Lead | Nairobi | Testing, presentation materials |

See [TEAM_ROLES_AND_DELIVERABLES.md](TEAM_ROLES_AND_DELIVERABLES.md) for full details.

## Milestones

- **Meeting 1**: Project planning and scope definition ✓
- **Meeting 2**: Repository setup and skeleton creation (Current)
- **Meeting 3**: AI integration and knowledge base implementation
- **Meeting 4**: Feature completion and integration testing
- **Meeting 5**: Final testing, polishing, and presentation

## Coding Standards

- Keep code simple and readable
- Use meaningful variable and function names
- Separate frontend and backend concerns
- Avoid code duplication
- Comment only when logic is non-obvious
- Use environment variables for secrets
- Follow TypeScript/Python type conventions

See [AGENTS.md](AGENTS.md) for detailed coding guidelines.

## Contributing

When contributing to this project:

1. Read PROJECT_SOURCE_OF_TRUTH.md to understand project scope
2. Check TEAM_ROLES_AND_DELIVERABLES.md for assignments
3. Follow AGENTS.md coding guidelines
4. Keep commits focused on single features
5. Write clear commit messages
6. Test changes before committing
7. Document changes if needed

## Future Enhancements

Post-course improvements under consideration:

- Multi-institution support
- User authentication and personalization
- Admin dashboard for knowledge management
- Analytics and usage insights
- Improved avatar quality and customization
- Voice conversation support
- Production deployment and scaling
- Advanced caching and performance optimization

## License

This project is developed for Centennial College Software Engineering Fundamentals course.

## Contact

For questions about the project, contact the project lead or visit the repository.

---

**Last Updated**: July 27, 2026  
**Repository**: [Link to GitHub repository]
