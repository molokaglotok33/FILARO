from sqlalchemy.orm import Session

from app.repositories.plan_repository import PlanRepository


class PlanService:
    def __init__(self, db: Session):
        self.repository = PlanRepository(db)

    def get_plans(self):
        return self.repository.get_all()