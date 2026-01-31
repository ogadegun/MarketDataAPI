"""
Main FastAPI application
"""
from fastapi import FastAPI
from app.core.config import get_settings
from app.api import routes

settings = get_settings()

app = FastAPI(
    title=settings.api_title,
    version=settings.api_version,
    description=settings.api_description
)

# Include API routes
app.include_router(routes.router)


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Market Data API",
        "version": settings.api_version,
        "documentation": "/docs",
        "health": "/health"
    }