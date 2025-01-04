from aiogram.types import (
    ForceReply,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

__all__ = ("ReplyMarkup", "TextView", "PhotoView", "View")


# FOR TYPE INSPECTION ONLY !!!
type ReplyMarkup = (
    InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply
)


class TextView:
    text: str
    reply_markup: ReplyMarkup | None = None
    disable_web_page_preview: bool | None = None

    def get_text(self) -> str:
        return self.text

    def get_reply_markup(self) -> ReplyMarkup | None:
        return self.reply_markup

    def get_disable_web_page_preview(self) -> bool | None:
        return self.disable_web_page_preview


class PhotoView:
    photo: str
    caption: str | None = None
    reply_markup: ReplyMarkup | None = None

    def get_photo(self) -> str:
        return self.photo

    def get_caption(self) -> str | None:
        return self.caption

    def get_reply_markup(self) -> ReplyMarkup | None:
        return self.reply_markup


# FOR TYPE INSPECTION ONLY !!!
type View = TextView | PhotoView
