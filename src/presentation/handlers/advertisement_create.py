from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from sqlalchemy.orm import Session

from application.callback_data import (
    ACCEPT_CALLBACK_DATA,
    REJECT_CALLBACK_DATA,
)
from application.interactors import (
    TemporaryMediaFileCreateInteractor,
    TemporaryMediaFilesDeleteAllInteractor,
    TemporaryMediaFilesReadInteractor,
    TemporaryMediaFileToCreate,
)
from application.states import AdvertisementCreateStates
from domain.exceptions.advertisements import AdvertisementTextLengthError
from domain.invariants.advertisements import validate_advertisement_text_length
from infrastructure.database.dao.temporary_media_files import (
    TemporaryMediaFileDAO,
)
from infrastructure.database.models import AdvertisementMediaFileType
from presentation.responses import answer_view, edit_as_rejected
from presentation.ui.buttons.texts import (
    ADVERTISEMENT_CREATE_FLOW_START_BUTTON_TEXT,
    CONTINUE_BUTTON_TEXT,
)
from presentation.ui.views import (
    AdvertisementCreateConfirmView,
    AdvertisementCreateMediaInputView,
    AdvertisementCreateTextInputView,
    AdvetisementCreateMediaUploadedView,
)
from presentation.ui.views.advertisement_create import (
    AdvertisementCreateMediaFilesView,
)

router = Router(name=__name__)


@router.message(
    F.text == ADVERTISEMENT_CREATE_FLOW_START_BUTTON_TEXT,
    StateFilter("*"),
)
async def on_advertisement_create_flow_start(
    message: Message,
    state: FSMContext,
) -> None:
    await state.set_state(AdvertisementCreateStates.text)
    view = AdvertisementCreateTextInputView()
    await answer_view(message, view)


@router.message(
    F.text,
    StateFilter(AdvertisementCreateStates.text),
)
async def on_advertisement_create_text_input(
    message: Message,
    state: FSMContext,
) -> None:
    message_text = message.html_text or ""

    try:
        validate_advertisement_text_length(message_text)
    except AdvertisementTextLengthError as error:
        await message.answer(
            f"❌ Длина описания не должна превышать {error.max_length} символов",
        )

    await state.set_state(AdvertisementCreateStates.media)
    await state.update_data(text=message_text)

    view = AdvertisementCreateMediaInputView()
    await answer_view(message, view)


@router.message(
    F.photo,
    StateFilter(AdvertisementCreateStates.media),
)
async def on_advertisement_create_media_input(
    message: Message,
    session: Session,
) -> None:
    user_id: int = message.from_user.id  # type: ignore [reportOptionalMemberAccess]
    photo = message.photo[-1]  # type: ignore [reportOptionalMemberAccess]

    temporary_media_file_dao = TemporaryMediaFileDAO(session)
    temporary_media_file_to_create = TemporaryMediaFileToCreate(
        user_id=user_id,
        telegram_id=photo.file_id,
        type=AdvertisementMediaFileType.PHOTO,
    )
    temporary_media_file_create_interactor = TemporaryMediaFileCreateInteractor(
        temporary_media_file_dao=temporary_media_file_dao,
        temporary_media_file=temporary_media_file_to_create,
    )
    temporary_media_file_create_interactor.execute()

    view = AdvetisementCreateMediaUploadedView(photo.file_id)
    await answer_view(message, view)


@router.message(
    F.text == CONTINUE_BUTTON_TEXT,
    StateFilter(AdvertisementCreateStates.media),
)
async def on_advertisement_create_media_input_finish(
    message: Message,
    state: FSMContext,
    session: Session,
) -> None:
    user_id: int = message.from_user.id  # type: ignore [reportOptionalMemberAccess]

    await state.set_state(AdvertisementCreateStates.confirm)
    temporary_media_file_dao = TemporaryMediaFileDAO(session)
    temporary_media_files_read_interactor = TemporaryMediaFilesReadInteractor(
        temporary_media_file_dao=temporary_media_file_dao,
        user_id=user_id,
    )
    user_temporary_media_files = temporary_media_files_read_interactor.execute()

    state_data: dict = await state.get_data()
    text: str = state_data["text"]

    view = AdvertisementCreateMediaFilesView(
        text=text,
        media_files=user_temporary_media_files.media_files,
    )
    await answer_view(message, view)

    view = AdvertisementCreateConfirmView()
    await answer_view(message, view)


@router.callback_query(
    F.data == ACCEPT_CALLBACK_DATA,
    StateFilter(AdvertisementCreateStates.confirm),
)
async def on_advertisement_create_confirm_accept(
    callback_query: CallbackQuery,
    state: FSMContext,
    session: Session,
) -> None:
    pass
    # temporary_media_file_dao = TemporaryMediaFileDAO(session)
    # temporary_media_files_read_interactor = TemporaryMediaFilesReadInteractor(
    #     temporary_media_file_dao=temporary_media_file_dao,
    #     user_id=callback_query.from_user.id,
    # )
    # user_temporary_media_files = temporary_media_files_read_interactor.execute()


@router.callback_query(
    F.data == REJECT_CALLBACK_DATA,
    StateFilter(AdvertisementCreateStates.confirm),
)
async def on_advertisement_create_confirm_reject(
    callback_query: CallbackQuery,
    state: FSMContext,
    session: Session,
) -> None:
    temporary_media_file_dao = TemporaryMediaFileDAO(session)
    temporary_media_files_delete_all_interactor = (
        TemporaryMediaFilesDeleteAllInteractor(
            temporary_media_file_dao=temporary_media_file_dao,
            user_id=callback_query.from_user.id,
        )
    )
    temporary_media_files_delete_all_interactor.execute()
    await state.clear()

    message: Message = callback_query.message  # type: ignore [reportOptionalMemberAccess]
    await edit_as_rejected(message)
