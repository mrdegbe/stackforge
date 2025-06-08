from fastapi import FastAPI
from src.backend.api import routes

app = FastAPI(title="StackForge API")

app.include_router(routes.router)

# Run with: uvicorn backend.main:app --reload
