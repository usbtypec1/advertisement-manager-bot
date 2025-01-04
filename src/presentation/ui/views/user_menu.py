from presentation.ui.views.base import TextView
from presentation.ui import markups, texts


__all__ = ("UserMenuView",)


class UserMenuView(TextView):
    text = texts.USER_MENU_TEXT
    reply_markup = markups.USER_MENU_MARKUP
