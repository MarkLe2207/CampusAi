from fastapi import APIRouter

router = APIRouter()


@router.get("/chat")
async def chat():
    """Chat endpoint - to be implemented"""
    return {
        "message": "Chat endpoint ready for implementation"
    }


@router.post("/query")
async def query():
    """Query endpoint - to be implemented"""
    return {
        "message": "Query endpoint ready for implementation"
    }
