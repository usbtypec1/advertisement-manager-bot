from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import StateFilter
from sqlalchemy.orm import Session

from presentation.responses import answer_view
from application.interactors import UserReadByIdInteractor
from infrastructure.database.dao.users import UserDAO
from presentation.ui.views import UserMenuView


__all__ = ("router",)


router = Router(name=__name__)


@router.message(
    F.text,
    StateFilter("*"),
)
async def on_show_main_menu(
    message: Message,
    session: Session,
) -> None:
    user_id = message.from_user.id  # type: ignore [reportOptionalMemberAccess]
    user_dao = UserDAO(session)
    interactor = UserReadByIdInteractor(user_dao=user_dao, user_id=user_id)
    interactor.execute()
    await answer_view(message, UserMenuView())
