from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from application.states import AdvertisementCreateStates
from presentation.ui.buttons.texts import ADVERTISEMENT_CREATE_FLOW_START_BUTTON_TEXT

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
    await state.update_data(text=message.html_text)
