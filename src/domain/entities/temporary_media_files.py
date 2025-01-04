import datetime
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, Field

from infrastructure.database.models import AdvertisementMediaFileType

__all__ = ("TemporaryMediaFile", "UserTemporaryMediaFiles")


class TemporaryMediaFile(BaseModel):
    id: UUID
    telegram_id: str
    type: AdvertisementMediaFileType
    created_at: datetime.datetime


class UserTemporaryMediaFiles(BaseModel):
    user_id: int
    media_files: Annotated[list[TemporaryMediaFile], Field(max_length=10)]
