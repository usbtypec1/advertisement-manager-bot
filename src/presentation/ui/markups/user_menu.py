from typing import Final

from aiogram.types import ReplyKeyboardMarkup

from presentation.ui.buttons.keyboard import (
    ADVERTISEMENT_CREATE_FLOW_START_BUTTON,
    SUPPORT_BUTTON,
)

__all__ = ("USER_MENU_MARKUP",)


USER_MENU_MARKUP: Final[ReplyKeyboardMarkup] = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [ADVERTISEMENT_CREATE_FLOW_START_BUTTON],
        [SUPPORT_BUTTON],
    ],
)
