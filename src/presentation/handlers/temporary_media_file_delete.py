from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery, Message, PhotoSize
from sqlalchemy.orm import Session

from application.callback_data import DELETE_CALLBACK_DATA
from application.interactors import TemporaryMediaFileDeleteByIDInteractor
from infrastructure.database.dao import TemporaryMediaFileDAO
from presentation.responses import answer_as_deleted

__all__ = ("router",)


router = Router(name=__name__)


@router.callback_query(
    F.data == DELETE_CALLBACK_DATA,
    F.message.photo.as_("photos"),
    StateFilter("*"),
)
async def on_temporary_media_file_delete(
    callback_query: CallbackQuery,
    photos: list[PhotoSize],
    session: Session,
) -> None:
    user_id: int = callback_query.from_user.id
    file_telegram_id: str = photos[-1].file_id

    message: Message = callback_query.message  # type: ignore [reportOptionalMemberAccess]

    temporary_media_file_dao = TemporaryMediaFileDAO(session)
    temporary_media_files_delete_interactor = TemporaryMediaFileDeleteByIDInteractor(
        temporary_media_file_dao=temporary_media_file_dao,
        user_id=user_id,
        file_telegram_id=file_telegram_id,
    )
    temporary_media_files_delete_interactor.execute()

    await answer_as_deleted(callback_query)
    await message.delete()
