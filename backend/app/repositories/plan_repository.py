from sqlalchemy.orm import Session

from app.models.plan import Plan


class PlanRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Plan]:
        return (
            self.db.query(Plan)
            .filter(Plan.active == True)
            .all()
        )