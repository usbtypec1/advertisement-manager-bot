from typing import Final

from aiogram.types import KeyboardButton

from presentation.ui.buttons import texts


__all__ = (
    "ADVERTISEMENT_CREATE_BUTTON",
    "SUPPORT_BUTTON",
    "USER_REGISTER_FLOW_START_BUTTON",
    "USER_REGISTER_INPUT_PHONE_NUMBER_BUTTON",
)


ADVERTISEMENT_CREATE_BUTTON: Final[KeyboardButton] = KeyboardButton(
    text=texts.ADVERTISEMENT_CREATE_BUTTON_TEXT,
)
SUPPORT_BUTTON: Final[KeyboardButton] = KeyboardButton(text=texts.SUPPORT_BUTTON_TEXT)
USER_REGISTER_FLOW_START_BUTTON: Final[KeyboardButton] = KeyboardButton(
    text=texts.USER_REGISTER_FLOW_START_BUTTON_TEXT
)
USER_REGISTER_INPUT_PHONE_NUMBER_BUTTON: Final[KeyboardButton] = KeyboardButton(
    text=texts.USER_REGISTER_PHONE_NUMBER_INPUT_BUTTON_TEXT,
    request_contact=True,
)
