from dataclasses import dataclass

from infrastructure.database.dao import TemporaryMediaFileDAO
from infrastructure.database.models import AdvertisementMediaFileType

__all__ = ("TemporaryMediaFileCreateInteractor", "TemporaryMediaFileToCreate")


@dataclass(slots=True)
class TemporaryMediaFileToCreate:
    user_id: int
    telegram_id: str
    type: AdvertisementMediaFileType


class TemporaryMediaFileCreateInteractor:
    def __init__(
        self,
        *,
        temporary_media_file_dao: TemporaryMediaFileDAO,
        temporary_media_file: TemporaryMediaFileToCreate,
    ) -> None:
        self.__temporary_media_file_dao = temporary_media_file_dao
        self.__temporary_media_file = temporary_media_file

    def execute(self) -> None:
        self.__temporary_media_file_dao.create(self.__temporary_media_file)
