from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.models.advertisement_media_file_types import (
    AdvertisementMediaFileType,
)
from infrastructure.database.models.base import Base

__all__ = ("TemporaryMediaFile",)


class TemporaryMediaFile(Base):
    __tablename__ = "temporary_media_files"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    telegram_id: Mapped[str] = mapped_column(String(255))
    type: Mapped[AdvertisementMediaFileType]

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    def __str__(self) -> str:
        return f"TemporaryMediaFile(id={self.id}, user_id={self.user_id}, telegram_id={self.telegram_id}, type={self.type})"
