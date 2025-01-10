from dataclasses import dataclass

from infrastructure.database.dao import (
    AdvertisementCreatedDTO,
    AdvertisementDAO,
)
from infrastructure.database.models import AdvertisementMediaFileType

__all__ = (
    "AdvertisementCreateInteractor",
    "AdvertisementMediaFileToCreateDTO",
    "AdvertisementToCreateDTO",
)


@dataclass(slots=True, kw_only=True)
class AdvertisementMediaFileToCreateDTO:
    telegram_id: str
    type: AdvertisementMediaFileType


@dataclass(slots=True, kw_only=True)
class AdvertisementToCreateDTO:
    text: str
    user_id: int
    media_files: list[AdvertisementMediaFileToCreateDTO]


@dataclass(slots=True, frozen=True, kw_only=True)
class AdvertisementCreateInteractor:
    advertisement_dao: AdvertisementDAO
    advertisement: AdvertisementToCreateDTO

    def execute(self) -> AdvertisementCreatedDTO:
        return self.advertisement_dao.create(
            advertisement=self.advertisement,
            media_files=self.advertisement.media_files,
        )
