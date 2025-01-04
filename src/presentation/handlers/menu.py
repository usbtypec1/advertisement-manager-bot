from aiogram import Router
from aiogram.types import Message
from aiogram.filters import StateFilter, CommandStart

from presentation.responses import answer_view


__all__ = ("router",)


router = Router(name=__name__)


@router.message(
    CommandStart(),
    StateFilter("*"),
)
async def on_show_main_menu(
    message: Message,
) -> None:
    await answer_view(
        message,
    )
