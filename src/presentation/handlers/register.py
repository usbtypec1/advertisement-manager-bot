from aiogram import F, Router
from aiogram.filters import ExceptionTypeFilter, StateFilter, or_f
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, ErrorEvent, Message

from application.callback_data import ACCEPT_CALLBACK_DATA
from application.states import UserRegisterStates
from domain.exceptions.users import UserNotFoundError
from presentation.responses import answer_view
from presentation.ui.buttons.texts import (
    SKIP_BUTTON_TEXT,
    USER_REGISTER_FLOW_START_BUTTON_TEXT,
)
from presentation.ui.views import (
    UserRegisterConfirmView,
    UserRegisterFlowStartView,
    UserRegisterPhoneNumberInputView,
)

__all__ = ("router",)


router = Router(name=__name__)


@router.error(
    ExceptionTypeFilter(UserNotFoundError),
)
async def on_user_not_found_error(event: ErrorEvent) -> None:
    if (message := event.update.message) is not None:
        await answer_view(message, UserRegisterFlowStartView())
    else:
        raise event.exception


@router.message(
    F.text == USER_REGISTER_FLOW_START_BUTTON_TEXT,
    StateFilter("*"),
)
async def on_start_user_register_flow(
    message: Message,
    state: FSMContext,
) -> None:
    await state.set_state(UserRegisterStates.phone_number)
    view = UserRegisterPhoneNumberInputView()
    await answer_view(message, view)


@router.message(
    or_f(
        F.contact,
        F.text == SKIP_BUTTON_TEXT,
    ),
    StateFilter(UserRegisterStates.phone_number),
)
async def on_user_register_phone_number_input(
    message: Message,
    state: FSMContext,
) -> None:
    if message.contact is not None:
        phone_number = message.contact.phone_number
    else:
        phone_number = None

    await state.update_data(phone_number=phone_number)
    await state.set_state(UserRegisterStates.confirm)

    view = UserRegisterConfirmView()
    await answer_view(message, view)


@router.callback_query(
    F.data == ACCEPT_CALLBACK_DATA,
    StateFilter(UserRegisterStates.confirm),
)
async def on_user_register_confirm_accept(
    callback_query: CallbackQuery,
    state: FSMContext,
) -> None:
    pass
