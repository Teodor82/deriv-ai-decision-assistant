"""Health check routes."""
from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/", name="Health Check")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "ok",
        "message": "Deriv AI Decision Assistant is running",
    }
