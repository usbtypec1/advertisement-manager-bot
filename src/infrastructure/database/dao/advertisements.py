import datetime
from collections.abc import Iterable
from dataclasses import dataclass
from typing import Protocol

from infrastructure.database.dao.base import DatabaseDAO
from infrastructure.database.models import (
    Advertisement,
    AdvertisementMediaFile,
    AdvertisementMediaFileType,
    AdvertisementStatus,
)

__all__ = (
    "AdvertisementMediaFileCreatedDTO",
    "AdvertisementCreatedDTO",
    "AdvertisementDAO",
)


class AdvertisementMediaFileToCreate(Protocol):
    telegram_id: str
    type: AdvertisementMediaFileType


class AdvertisementToCreate(Protocol):
    text: str
    user_id: int


@dataclass(frozen=True, slots=True, kw_only=True)
class AdvertisementMediaFileCreatedDTO:
    telegram_id: str
    type: AdvertisementMediaFileType


@dataclass(frozen=True, slots=True, kw_only=True)
class AdvertisementCreatedDTO:
    id: int
    text: str
    user_id: int
    status: AdvertisementStatus
    media_files: list[AdvertisementMediaFileCreatedDTO]
    created_at: datetime.datetime


class AdvertisementDAO(DatabaseDAO):
    def create(
        self,
        *,
        advertisement: AdvertisementToCreate,
        media_files: Iterable[AdvertisementMediaFileToCreate],
    ) -> AdvertisementCreatedDTO:
        advertisement_to_create = Advertisement(
            text=advertisement.text, user_id=advertisement.user_id
        )
        media_files_to_create = [
            AdvertisementMediaFile(
                telegram_id=media_file.telegram_id,
                type=media_file.type,
                advertisement=advertisement_to_create,
            )
            for media_file in media_files
        ]

        with self._session.begin(nested=True):
            self._session.add(advertisement_to_create)
            self._session.add_all(media_files_to_create)
            self._session.commit()

        return AdvertisementCreatedDTO(
            id=advertisement_to_create.id,
            text=advertisement_to_create.text,
            user_id=advertisement_to_create.user_id,
            status=advertisement_to_create.status,
            created_at=advertisement_to_create.created_at,
            media_files=[
                AdvertisementMediaFileCreatedDTO(
                    telegram_id=media_file.telegram_id,
                    type=media_file.type,
                )
                for media_file in media_files_to_create
            ],
        )
