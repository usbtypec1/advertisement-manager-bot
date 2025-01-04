from typing import Final

from aiogram.types import ReplyKeyboardMarkup

from presentation.ui.buttons.keyboard import (
    USER_REGISTER_FLOW_START_BUTTON,
    USER_REGISTER_INPUT_PHONE_NUMBER_BUTTON,
    SKIP_BUTTON,
)


__all__ = (
    "USER_REGISTER_FLOW_START_MARKUP",
    "USER_REGISTER_PHONE_NUMBER_INPUT_MARKUP",
)


USER_REGISTER_FLOW_START_MARKUP: Final[ReplyKeyboardMarkup] = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[[USER_REGISTER_FLOW_START_BUTTON]],
)


USER_REGISTER_PHONE_NUMBER_INPUT_MARKUP: Final[ReplyKeyboardMarkup] = (
    ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                USER_REGISTER_INPUT_PHONE_NUMBER_BUTTON,
            ],
            [
                SKIP_BUTTON,
            ],
        ],
    )
)
