from aiogram.types import (
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
)


__all__ = ("ReplyMarkup", "TextView", "View")


type ReplyMarkup = (
    InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply
)


class TextView:
    text: str
    reply_markup: ReplyMarkup | None = None

    def get_text(self) -> str:
        return self.text

    def get_reply_markup(self) -> ReplyMarkup | None:
        return self.reply_markup


type View = TextView
