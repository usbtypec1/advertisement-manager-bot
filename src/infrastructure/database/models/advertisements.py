from datetime import datetime
from enum import IntEnum

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from infrastructure.database.models.base import Base


__all__ = (
    "Advertisement",
    "AdvertisementStatus",
    "AdvertisementMediaFile",
    "AdvertisementMediaFileType",
)


class AdvertisementMediaFileType(IntEnum):
    PHOTO = 1
    VIDEO = 2


class AdvertisementStatus(IntEnum):
    PENDING = 1
    PUBLISHED = 2
    DELETED = 3
    REJECTED = 4


class AdvertisementMediaFile(Base):
    __tablename__ = "advertisement_media_files"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[str] = mapped_column(String(255))
    type: Mapped[AdvertisementMediaFileType]
    advertisement_id: Mapped[int] = mapped_column(
        ForeignKey("advertisements.id", ondelete="CASCADE")
    )

    advertisement: Mapped["Advertisement"] = relationship(
        "Advertisement", back_populates="media_files"
    )

    def __repr__(self) -> str:
        return f"AdvertisementMediaFile(id={self.id!r}, telegram_id={self.telegram_id!r}, type={self.type!r}, advertisement_id={self.advertisement_id!r})"


class Advertisement(Base):
    __tablename__ = "advertisements"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(String(1024))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    status: Mapped[AdvertisementStatus] = mapped_column(
        default=AdvertisementStatus.PENDING
    )
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    media_files: Mapped[list[AdvertisementMediaFile]] = relationship(
        "AdvertisementMediaFile",
        back_populates="advertisement",
    )
