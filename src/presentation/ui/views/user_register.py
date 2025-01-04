from presentation.ui.views.base import TextView
from presentation.ui import markups, texts


__all__ = ("UserRegisterFlowStartView",)


class UserRegisterFlowStartView(TextView):
    text = texts.USER_REGISTER_FLOW_START_TEXT
    reply_markup = markups.USER_REGISTER_FLOW_START_MARKUP
