from pydantic import BaseModel
from typing import Optional


class ResponseModel(BaseModel):
    """Base response model for all API responses"""
    success: bool
    data: Optional[dict] = None
    message: str = "Success"
    error: Optional[str] = None


class ErrorResponse(BaseModel):
    """Error response model"""
    success: bool = False
    error: str
    message: str
