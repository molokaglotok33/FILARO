from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    telegram_id: int
    username: str | None
    first_name: str
    created_at: datetime