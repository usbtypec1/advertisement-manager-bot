from dataclasses import dataclass

from domain.entities.temporary_media_files import (
    TemporaryMediaFile,
    UserTemporaryMediaFiles,
)
from infrastructure.database.dao.temporary_media_files import (
    TemporaryMediaFileDAO,
)

__all__ = ("TemporaryMediaFilesReadInteractor",)


@dataclass(frozen=True, slots=True)
class TemporaryMediaFilesReadInteractor:
    temporary_media_file_dao: TemporaryMediaFileDAO
    user_id: int

    def execute(self) -> UserTemporaryMediaFiles:
        temporary_media_files = self.temporary_media_file_dao.get_all(
            user_id=self.user_id
        )

        temporary_media_files = [
            TemporaryMediaFile(
                id=media_file.id,
                telegram_id=media_file.telegram_id,
                type=media_file.type,
                created_at=media_file.created_at,
            )
            for media_file in temporary_media_files
        ]

        return UserTemporaryMediaFiles(
            user_id=self.user_id,
            media_files=temporary_media_files,
        )
