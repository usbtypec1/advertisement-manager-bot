from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from application.states import AdvertisementCreateStates
from domain.exceptions.advertisements import AdvertisementTextLengthError
from domain.invariants.advertisements import validate_advertisement_text_length
from presentation.responses import answer_view
from presentation.ui.buttons.texts import (
    ADVERTISEMENT_CREATE_FLOW_START_BUTTON_TEXT,
)
from presentation.ui.views import AdvertisementCreateTextInputView
from presentation.ui.views.advertisement_create import (
    AdvertisementCreateMediaInputView,
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
    StateFilter("*"),
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
