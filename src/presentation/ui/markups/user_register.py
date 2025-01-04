from typing import Final

from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup

from application.callback_data import ACCEPT_CALLBACK_DATA, REJECT_CALLBACK_DATA
from presentation.ui.buttons.inline import (
    create_accept_inline_button,
    create_reject_inline_button,
)
from presentation.ui.buttons.keyboard import (
    SKIP_BUTTON,
    USER_REGISTER_FLOW_START_BUTTON,
    USER_REGISTER_INPUT_PHONE_NUMBER_BUTTON,
)

__all__ = (
    "USER_REGISTER_FLOW_START_MARKUP",
    "USER_REGISTER_PHONE_NUMBER_INPUT_MARKUP",
    "USER_REGISTER_CONFIRM_MARKUP",
)


USER_REGISTER_FLOW_START_MARKUP: Final[ReplyKeyboardMarkup] = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[[USER_REGISTER_FLOW_START_BUTTON]],
    one_time_keyboard=True,
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
        one_time_keyboard=True,
    )
)

USER_REGISTER_CONFIRM_MARKUP: Final[InlineKeyboardMarkup] = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            create_reject_inline_button(REJECT_CALLBACK_DATA),
            create_accept_inline_button(ACCEPT_CALLBACK_DATA),
        ],
    ],
)
