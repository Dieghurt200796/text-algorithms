from fastapi import FastAPI
from src.api.v1.routers import endpoints

app = FastAPI(title="Word Analysis API")
app.include_router(endpoints.router, prefix="/api/v1", tags=["Text"])