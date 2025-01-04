from datetime import datetime
from enum import IntEnum

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from infrastructure.database.models.base import Base


__all__ = ("Advertisement", "AdvertisementStatus")


class AdvertisementStatus(IntEnum):
    PENDING = 1
    PUBLISHED = 2
    DELETED = 3
    REJECTED = 4


class Advertisement(Base):
    __tablename__ = "advertisements"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(String(1024))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    status: Mapped[AdvertisementStatus] = mapped_column(
        default=AdvertisementStatus.PENDING
    )
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    user = relationship("User", back_populates="advertisements")
