from fastapi import FastAPI

app = FastAPI(
    title="FILARO API",
    description="Backend API for FILARO VPN SaaS",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {
        "project": "FILARO",
        "status": "online",
        "message": "Welcome to FILARO API 🚀",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }