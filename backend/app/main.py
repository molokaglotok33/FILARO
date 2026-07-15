from fastapi import FastAPI
from sqlalchemy import text

from app.api.router import router
from app.db.database import engine

app = FastAPI(
    title="FILARO API",
    description="Backend API for FILARO VPN SaaS",
    version="1.0.0",
)

app.include_router(router)

@app.on_event("startup")
async def startup():

    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    print("✅ PostgreSQL connected")
    
@app.get("/")
async def root():
    return {
        "project": "FILARO",
        "status": "online",
        "message": "Welcome to FILARO API 🚀",
    }