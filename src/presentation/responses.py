from aiogram.types import Message

from presentation.ui.views.base import TextView, View

__all__ = (
    "answer_text_view",
    "answer_view",
    "edit_as_accepted",
    "edit_as_rejected",
)


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


async def edit_as_accepted(message: Message) -> None:
    await message.edit_text(f"{message.text}\n\n✅ Подтверждено")


async def edit_as_rejected(message: Message) -> None:
    await message.edit_text(f"{message.text}\n\n❌ Отклонено")
