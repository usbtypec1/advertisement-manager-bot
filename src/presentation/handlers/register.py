from aiogram import Router
from aiogram.filters import ExceptionTypeFilter
from aiogram.types import ErrorEvent

from domain.exceptions.users import UserNotFoundError
from presentation.responses import answer_view
from presentation.ui.views import UserRegisterFlowStartView


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
