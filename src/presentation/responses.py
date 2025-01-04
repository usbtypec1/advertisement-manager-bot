from aiogram.types import Message

from presentation.ui.views.base import View, TextView


__all__ = ("answer_text_view", "answer_view")


async def answer_text_view(message: Message, view: TextView) -> None:
    await message.answer(
        text=view.get_text(),
        reply_markup=view.get_reply_markup(),
        disable_web_page_preview=view.get_disable_web_page_preview(),
    )


async def answer_view(message: Message, view: View) -> None:
    match view:
        case TextView():
            await answer_text_view(message, view)
