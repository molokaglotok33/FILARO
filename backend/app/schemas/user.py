from datetime import datetime

from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    telegram_id: int
    username: str | None = None
    first_name: str


class UserResponse(BaseModel):
    telegram_id: int
    username: str | None
    first_name: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)