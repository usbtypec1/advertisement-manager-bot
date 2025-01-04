from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from infrastructure.database.models.base import Base


__all__ = ("User",)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    full_name: Mapped[str] = mapped_column(String(64))
    username: Mapped[str | None] = mapped_column(String(32))
    phone_number: Mapped[str | None] = mapped_column(String(32))
    is_banned: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.utcnow())

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, full_name={self.full_name!r}, username={self.username!r}, phone_number={self.phone_number!r}, is_banned={self.is_banned!r}, created_at={self.created_at!r})"
