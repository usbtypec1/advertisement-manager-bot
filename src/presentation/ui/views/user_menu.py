from presentation.ui import markups, texts
from presentation.ui.views.base import TextView

__all__ = ("UserMenuView",)


class UserMenuView(TextView):
    text = texts.USER_MENU_TEXT
    reply_markup = markups.USER_MENU_MARKUP
