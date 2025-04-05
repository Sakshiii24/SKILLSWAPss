from fastapi import FastAPI
from app.routes import match  # Import your route module

app = FastAPI(
    title="Skill Swap API",
    description="Backend for matching users based on skill exchange",
    version="1.0.0"
)

# Register the router
app.include_router(match.router)
