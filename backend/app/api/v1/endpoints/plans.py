from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.services.plan_service import PlanService


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_plans(db: Session = Depends(get_db)):
    service = PlanService(db)
    return service.get_plans()