from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def register_user(
        self,
        telegram_id: int,
        username: str | None,
        first_name: str,
    ) -> User:

        user = self.repository.get_by_telegram_id(telegram_id)

        if user:
            return user

        return self.repository.create(
            telegram_id=telegram_id,
            username=username,
            first_name=first_name,
        )