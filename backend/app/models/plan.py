from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Plan(Base):
    __tablename__ = "plans"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
    )

    price: Mapped[int] = mapped_column(
        Integer,
    )

    days: Mapped[int] = mapped_column(
        Integer,
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )