from aiogram.types import CallbackQuery, Message

from presentation.ui.views.base import MediaGroupView, PhotoView, TextView, View

__all__ = (
    "answer_text_view",
    "answer_view",
    "answer_photo_view",
    "answer_media_group_view",
    "edit_as_accepted",
    "edit_as_rejected",
    "answer_as_deleted",
    "answer_as_rejected",
)


async def answer_text_view(message: Message, view: TextView) -> Message:
    return await message.answer(
        text=view.get_text(),
        reply_markup=view.get_reply_markup(),
        disable_web_page_preview=view.get_disable_web_page_preview(),
    )


async def answer_photo_view(message: Message, view: PhotoView) -> Message:
    return await message.answer_photo(
        photo=view.get_photo(),
        caption=view.get_caption(),
        reply_markup=view.get_reply_markup(),
    )


async def answer_media_group_view(
    message: Message, view: MediaGroupView
) -> list[Message]:
    return await message.answer_media_group(view.as_media_group())


async def answer_view(message: Message, view: View) -> Message | list[Message]:
    match view:
        case TextView():
            return await answer_text_view(message, view)
        case PhotoView():
            return await answer_photo_view(message, view)
        case MediaGroupView():
            return await answer_media_group_view(message, view)


async def edit_as_accepted(message: Message) -> None:
    await message.edit_text(f"{message.text}\n\n✅ Подтверждено")


async def edit_as_rejected(message: Message) -> None:
    await message.edit_text(f"{message.text}\n\n❌ Отклонено")


async def answer_as_deleted(callback_query: CallbackQuery) -> None:
    await callback_query.answer(text="❗️ Удалено", show_alert=True)


async def answer_as_rejected(callback_query: CallbackQuery) -> None:
    await callback_query.answer(text="❌ Отклонено", show_alert=True)
