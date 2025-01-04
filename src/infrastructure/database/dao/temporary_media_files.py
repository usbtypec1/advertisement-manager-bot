import datetime
from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from sqlalchemy import select

from infrastructure.database.dao.base import DatabaseDAO
from infrastructure.database.models import (
    AdvertisementMediaFileType,
    TemporaryMediaFile,
)

__all__ = (
    "TemporaryMediaFileToCreate",
    "TemporaryMediaFileDTO",
    "TemporaryMediaFileDAO",
)


class TemporaryMediaFileToCreate(Protocol):
    user_id: int
    telegram_id: str
    type: AdvertisementMediaFileType


@dataclass(frozen=True, slots=True)
class TemporaryMediaFileDTO:
    id: UUID
    user_id: int
    telegram_id: str
    type: AdvertisementMediaFileType
    created_at: datetime.datetime


class TemporaryMediaFileDAO(DatabaseDAO):
    def create(
        self,
        media_file: TemporaryMediaFileToCreate,
    ):
        temporary_media_file = TemporaryMediaFile(
            user_id=media_file.user_id,
            telegram_id=media_file.telegram_id,
            type=media_file.type,
        )
        with self._session.begin():
            self._session.add(temporary_media_file)
            self._session.commit()
            self._session.flush()

        return TemporaryMediaFileDTO(
            id=temporary_media_file.id,  # type: ignore [reportAssignmentType]
            user_id=temporary_media_file.user_id,
            telegram_id=temporary_media_file.telegram_id,
            type=temporary_media_file.type,
            created_at=temporary_media_file.created_at,
        )

    def get_all(self, user_id: int) -> list[TemporaryMediaFileDTO]:
        statement = select(TemporaryMediaFile).where(
            TemporaryMediaFile.user_id == user_id
        )

        result = self._session.scalars(statement)

        return [
            TemporaryMediaFileDTO(
                id=media_file.id,  # type: ignore [reportAssignmentType]
                user_id=media_file.user_id,
                telegram_id=media_file.telegram_id,
                type=media_file.type,
                created_at=media_file.created_at,
            )
            for media_file in result
        ]
