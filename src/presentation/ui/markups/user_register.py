from typing import Final

from aiogram.types import ReplyKeyboardMarkup

from presentation.ui.buttons.keyboard import USER_REGISTER_FLOW_START_BUTTON


__all__ = ("USER_REGISTER_FLOW_START_MARKUP",)


USER_REGISTER_FLOW_START_MARKUP: Final[ReplyKeyboardMarkup] = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[[USER_REGISTER_FLOW_START_BUTTON]],
)
