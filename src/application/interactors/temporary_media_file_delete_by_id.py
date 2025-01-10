from dataclasses import dataclass

from infrastructure.database.dao.temporary_media_files import (
    TemporaryMediaFileDAO,
)

__all__ = ("TemporaryMediaFilesDeleteByIDInteractor",)


@dataclass(frozen=True, slots=True, kw_only=True)
class TemporaryMediaFilesDeleteByIDInteractor:
    temporary_media_file_dao: TemporaryMediaFileDAO
    user_id: int
    file_telegram_id: str

    def execute(self) -> None:
        self.temporary_media_file_dao.delete_by_id(
            user_id=self.user_id,
            file_telegram_id=self.file_telegram_id,
        )
