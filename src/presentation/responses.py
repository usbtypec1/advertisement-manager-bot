from aiogram.types import Message

from presentation.ui.views.base import PhotoView, TextView, View

__all__ = (
    "answer_text_view",
    "answer_view",
    "answer_photo_view",
    "edit_as_accepted",
    "edit_as_rejected",
)


async def answer_text_view(message: Message, view: TextView) -> None:
    await message.answer(
        text=view.get_text(),
        reply_markup=view.get_reply_markup(),
        disable_web_page_preview=view.get_disable_web_page_preview(),
    )


async def answer_photo_view(message: Message, view: PhotoView) -> None:
    await message.answer_photo(
        photo=view.get_photo(),
        reply_markup=view.get_reply_markup(),
    )


async def answer_view(message: Message, view: View) -> None:
    match view:
        case TextView():
            await answer_text_view(message, view)
        case PhotoView():
            await answer_photo_view(message, view)


async def edit_as_accepted(message: Message) -> None:
    await message.edit_text(f"{message.text}\n\n✅ Подтверждено")


async def edit_as_rejected(message: Message) -> None:
    await message.edit_text(f"{message.text}\n\n❌ Отклонено")
