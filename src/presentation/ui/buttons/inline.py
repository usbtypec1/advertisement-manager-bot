from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton

from presentation.ui.buttons.texts import ACCEPT_BUTTON_TEXT, REJECT_BUTTON_TEXT

__all__ = ("create_accept_inline_button", "create_reject_inline_button")


def create_accept_inline_button(
    callback_data: CallbackData | str,
) -> InlineKeyboardButton:
    if isinstance(callback_data, CallbackData):
        callback_data = callback_data.pack()
    return InlineKeyboardButton(
        text=ACCEPT_BUTTON_TEXT,
        callback_data=callback_data,
    )


def create_reject_inline_button(
    callback_data: CallbackData | str,
) -> InlineKeyboardButton:
    if isinstance(callback_data, CallbackData):
        callback_data = callback_data.pack()
    return InlineKeyboardButton(
        text=REJECT_BUTTON_TEXT,
        callback_data=callback_data,
    )
