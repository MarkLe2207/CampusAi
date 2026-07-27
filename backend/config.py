from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # API Configuration
    API_TITLE: str = "CampusAI API"
    API_VERSION: str = "0.1.0"
    DEBUG: bool = True

    # Server Configuration
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    RELOAD: bool = True

    # CORS Configuration
    FRONTEND_URL: str = "http://localhost:3000"
    ALLOWED_ORIGINS: list = ["http://localhost:3000", "http://localhost:8000"]

    # LLM Configuration
    LLM_PROVIDER: str = "ollama"  # ollama or openai
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "mistral"  # Default model
    OPENAI_API_KEY: Optional[str] = None

    # Vector Database Configuration
    CHROMA_DB_PATH: str = "./chromadb_data"
    CHROMA_COLLECTION_NAME: str = "college_knowledge"

    # Knowledge Base Configuration
    KNOWLEDGE_BASE_PATH: str = "../knowledge"

    # Environment
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
