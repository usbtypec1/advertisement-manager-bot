from dataclasses import dataclass

from infrastructure.database.dao.temporary_media_files import (
    TemporaryMediaFileDAO,
)

__all__ = ("TemporaryMediaFilesDeleteAllInteractor",)


@dataclass(frozen=True, slots=True, kw_only=True)
class TemporaryMediaFilesDeleteAllInteractor:
    temporary_media_file_dao: TemporaryMediaFileDAO
    user_id: int

    def execute(self) -> None:
        self.temporary_media_file_dao.delete_all(self.user_id)
