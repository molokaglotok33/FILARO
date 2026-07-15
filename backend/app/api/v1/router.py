from fastapi import APIRouter

from app.api.v1.endpoints import health, users, plans

router = APIRouter()

router.include_router(
    health.router,
    prefix="/health",
    tags=["Health"],
)

router.include_router(
    users.router,
    prefix="/users",
    tags=["Users"],
)

router.include_router(
    plans.router,
    prefix="/plans",
    tags=["Plans"],
)