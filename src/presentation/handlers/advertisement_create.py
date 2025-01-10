from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy.orm import Session

from application.interactors.temporary_media_files_read import (
    TemporaryMediaFilesReadInteractor,
)
from application.states import AdvertisementCreateStates
from domain.exceptions.advertisements import AdvertisementTextLengthError
from domain.invariants.advertisements import validate_advertisement_text_length
from infrastructure.database.dao.temporary_media_files import (
    TemporaryMediaFileDAO,
)
from presentation.responses import answer_view
from presentation.ui.buttons.texts import (
    ADVERTISEMENT_CREATE_FLOW_START_BUTTON_TEXT,
    CONTINUE_BUTTON_TEXT,
)
from presentation.ui.views import (
    AdvertisementCreateConfirmView,
    AdvertisementCreateMediaInputView,
    AdvertisementCreateTextInputView,
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


# @router.message(
#     F.photo,
#     StateFilter(AdvertisementCreateStates.media),
# )
# async def on_advertisement_create_media_input(
#     message: Message,
#     state: FSMContext,
# ) -> None:
#     pass


# @router.callback_query(
#     F.data,
#     StateFilter(AdvertisementCreateStates.confirm),
# )
# async def on_advertisement_create_confirm_accept(
#     callback_query: CallbackQuery,
#     state: FSMContext,
#     session: Session,
# ) -> None:
#     temporary_media_file_dao = TemporaryMediaFileDAO(session)
# temporary_media_files_read_interactor = TemporaryMediaFilesReadInteractor(
#     temporary_media_file_dao=temporary_media_file_dao,
#     user_id=callback_query.from_user.id,
# )
# user_temporary_media_files = temporary_media_files_read_interactor.execute()
