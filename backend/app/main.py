from fastapi import FastAPI

from app.api.router import router

app = FastAPI(
    title="FILARO API",
    description="Backend API for FILARO VPN SaaS",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
async def root():
    return {
        "project": "FILARO",
        "status": "online",
        "message": "Welcome to FILARO API 🚀",
    }