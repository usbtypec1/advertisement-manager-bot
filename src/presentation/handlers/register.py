from aiogram import Router
from aiogram.filters import ExceptionTypeFilter
from aiogram.types import ErrorEvent

from domain.exceptions.users import UserNotFoundError


__all__ = ("router",)


router = Router(name=__name__)


@router.error(
    ExceptionTypeFilter(UserNotFoundError),
)
async def on_user_not_found_error(event: ErrorEvent) -> None:
    pass
