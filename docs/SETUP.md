# Development Setup Guide

## Prerequisites

- Node.js 18+ and npm
- Python 3.11+
- Git
- Docker (optional, for Ollama)

## Frontend Setup

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Environment Configuration

```bash
# Copy example env file
cp .env.example .env.local

# Edit .env.local with your configuration
```

### 3. Run Development Server

```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## Backend Setup

### 1. Create Virtual Environment

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration

```bash
# Copy example env file
cp .env.example .env

# Edit .env with your configuration
```

### 4. Run Development Server

```bash
python main.py
```

The backend API will be available at `http://localhost:8000`

API documentation: `http://localhost:8000/docs`

## Ollama Setup (Local LLM)

### Option 1: Docker

```bash
docker pull ollama/ollama
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
docker exec -it ollama ollama pull mistral
```

### Option 2: Direct Installation

Download and install from: https://ollama.ai

Then pull a model:
```bash
ollama pull mistral
```

## Verification

### Frontend
- Navigate to http://localhost:3000
- Verify page loads without errors

### Backend
- Navigate to http://localhost:8000/health
- Should return `{"status": "ok"}`

### API Documentation
- Navigate to http://localhost:8000/docs
- Should display Swagger UI

## Troubleshooting

### Port Already in Use
- Frontend (3000): Change in `next.config.js`
- Backend (8000): Change PORT in `.env`

### Module Not Found
- Make sure you've installed dependencies: `npm install` and `pip install -r requirements.txt`

### Environment Variables
- Ensure `.env` and `.env.local` files are properly configured
- Never commit `.env` files

## Next Steps

1. Complete frontend and backend setup
2. Verify both servers are running
3. Test API connection from frontend to backend
4. Begin feature development
