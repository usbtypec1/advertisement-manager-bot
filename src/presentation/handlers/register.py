from aiogram import F, Router
from aiogram.filters import ExceptionTypeFilter, StateFilter, or_f
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, ErrorEvent, Message
from sqlalchemy.orm import Session

from application.callback_data import ACCEPT_CALLBACK_DATA, REJECT_CALLBACK_DATA
from application.interactors.user_create import (
    UserCreateInteractor,
    UserToCreate,
)
from application.states import UserRegisterStates
from domain.exceptions.users import UserNotFoundError
from infrastructure.database.dao.users import UserDAO
from presentation.responses import (
    answer_view,
    edit_as_accepted,
    edit_as_rejected,
)
from presentation.ui.buttons.texts import (
    SKIP_BUTTON_TEXT,
    USER_REGISTER_FLOW_START_BUTTON_TEXT,
)
from presentation.ui.views import (
    UserRegisterConfirmView,
    UserRegisterFlowStartView,
    UserRegisterPhoneNumberInputView,
)
from presentation.ui.views.user_menu import UserMenuView

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
    session: Session,
) -> None:
    state_data: dict = await state.get_data()

    message: Message = callback_query.message  # type: ignore [reportOptionalMemberAccess]

    user_id = callback_query.from_user.id
    full_name = callback_query.from_user.full_name
    username = callback_query.from_user.username
    phone_number: str | None = state_data["phone_number"]

    user_dao = UserDAO(session)

    user_to_create = UserToCreate(
        id=user_id,
        full_name=full_name,
        username=username,
        phone_number=phone_number,
    )
    interactor = UserCreateInteractor(user_dao=user_dao, user=user_to_create)
    interactor.execute()

    view = UserMenuView()
    await edit_as_accepted(message)
    await answer_view(message, view)


@router.callback_query(
    F.data == REJECT_CALLBACK_DATA,
    StateFilter(UserRegisterStates.confirm),
)
async def on_user_register_confirm_reject(
    callback_query: CallbackQuery,
    state: FSMContext,
) -> None:
    await state.clear()

    message: Message = callback_query.message  # type: ignore [reportOptionalMemberAccess]
    await edit_as_rejected(message)
    await message.edit_text("☺️ Ждем вас если передумаете")
