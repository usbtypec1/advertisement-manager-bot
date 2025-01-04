from aiogram.types import ForceReply, InlineKeyboardMarkup, ReplyKeyboardMarkup

from presentation.ui.buttons.inline import DELETE_BUTTON
from presentation.ui.buttons.keyboard import CONTINUE_BUTTON

__all__ = (
    "ADVERTISEMENT_CREATE_TEXT_INPUT_MARKUP",
    "ADVERTISEMENT_CREATE_PHOTO_INPUT_MARKUP",
    "ADVERTISEMENT_CREATE_SPECIFIC_PHOTO_MARKUP",
)


ADVERTISEMENT_CREATE_TEXT_INPUT_MARKUP = ForceReply(
    input_field_placeholder="Описание",
)
ADVERTISEMENT_CREATE_PHOTO_INPUT_MARKUP = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[[CONTINUE_BUTTON]],
)
ADVERTISEMENT_CREATE_SPECIFIC_PHOTO_MARKUP = InlineKeyboardMarkup(
    inline_keyboard=[[DELETE_BUTTON]],
)
