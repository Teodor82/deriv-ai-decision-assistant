# Use a lifespan context manager instead of deprecated on_event handlers
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.health import router as health_router
from routes.analyze import router as analyze_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager replacing deprecated startup/shutdown events."""
    print("🚀 Deriv AI Decision Assistant started")
    try:
        yield
    finally:
        print("🛑 Deriv AI Decision Assistant stopped")


app = FastAPI(
    title="Deriv AI Decision Assistant",
    description="API for analyzing market data using AI",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health_router)
app.include_router(analyze_router)


# Lifespan handles startup/shutdown printing now.


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
