from enum import IntEnum

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.models.base import Base
from infrastructure.database.models.advertisements import Advertisement


__all__ = ("AdvertisementMediaFile", "AdvertisementMediaFileType")


class AdvertisementMediaFileType(IntEnum):
    PHOTO = 1
    VIDEO = 2


class AdvertisementMediaFile(Base):
    __tablename__ = "advertisements"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[str] = mapped_column(String(255))
    type: Mapped[AdvertisementMediaFileType]
    advertisement_id: Mapped[int] = mapped_column(
        ForeignKey("advertisements.id", ondelete="CASCADE")
    )

    advertisement: Mapped[Advertisement] = relationship(
        "Advertisement", back_populates="media_files"
    )

    def __repr__(self) -> str:
        return f"AdvertisementMediaFile(id={self.id!r}, telegram_id={self.telegram_id!r}, type={self.type!r}, advertisement_id={self.advertisement_id!r})"
