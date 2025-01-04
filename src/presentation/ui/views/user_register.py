from presentation.ui import markups, texts
from presentation.ui.views.base import TextView

__all__ = (
    "UserRegisterFlowStartView",
    "UserRegisterPhoneNumberInputView",
    "UserRegisterConfirmView",
)


class UserRegisterFlowStartView(TextView):
    text = texts.USER_REGISTER_FLOW_START_TEXT
    reply_markup = markups.USER_REGISTER_FLOW_START_MARKUP


class UserRegisterPhoneNumberInputView(TextView):
    text = texts.USER_REGISTER_PHONE_NUMBER_INPUT_TEXT
    reply_markup = markups.USER_REGISTER_PHONE_NUMBER_INPUT_MARKUP


class UserRegisterConfirmView(TextView):
    text = texts.USER_REGISTER_CONFIRM_TEXT
    reply_markup = markups.USER_REGISTER_CONFIRM_MARKUP
    disable_web_page_preview = True
