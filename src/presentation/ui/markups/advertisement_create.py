from typing import Final

from aiogram.types import ForceReply, InlineKeyboardMarkup, ReplyKeyboardMarkup

from application.callback_data import ACCEPT_CALLBACK_DATA, REJECT_CALLBACK_DATA
from presentation.ui.buttons.inline import (
    DELETE_BUTTON,
    create_accept_inline_button,
    create_reject_inline_button,
)
from presentation.ui.buttons.keyboard import CONTINUE_BUTTON

__all__ = (
    "ADVERTISEMENT_CREATE_TEXT_INPUT_MARKUP",
    "ADVERTISEMENT_CREATE_MEDIA_INPUT_MARKUP",
    "ADVERTISEMENT_CREATE_MEDIA_UPLOADED_MARKUP",
    "ADVERTISEMENT_CREATE_CONFIRM_MARKUP",
)


ADVERTISEMENT_CREATE_TEXT_INPUT_MARKUP = ForceReply(
    input_field_placeholder="Описание",
)
ADVERTISEMENT_CREATE_MEDIA_INPUT_MARKUP = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[[CONTINUE_BUTTON]],
)
ADVERTISEMENT_CREATE_MEDIA_UPLOADED_MARKUP = InlineKeyboardMarkup(
    inline_keyboard=[[DELETE_BUTTON]],
)
ADVERTISEMENT_CREATE_CONFIRM_MARKUP: Final[InlineKeyboardMarkup] = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            create_reject_inline_button(REJECT_CALLBACK_DATA),
            create_accept_inline_button(ACCEPT_CALLBACK_DATA),
        ],
    ],
)
