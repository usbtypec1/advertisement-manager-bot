from typing import Final


__all__ = (
    "USER_MENU_TEXT",
    "USER_REGISTER_FLOW_START_TEXT",
    "USER_REGISTER_PHONE_NUMBER_INPUT_TEXT",
    "USER_REGISTER_CONFIRM_TEXT",
    "USER_AGREEMENT_URL",
)


USER_AGREEMENT_URL = "https://graph.org/Polzovatelskoe-soglashenie-01-04-6"

USER_MENU_TEXT: Final[str] = "📲 Главное меню"
USER_REGISTER_FLOW_START_TEXT: Final[str] = (
    "🙂 Зарегистрируйтесь чтобы использовать бота"
)
USER_REGISTER_PHONE_NUMBER_INPUT_TEXT: Final[str] = "📲 Введите ваш номер телефона"
USER_REGISTER_CONFIRM_TEXT: Final[str] = (
    "❗️ Вы уверены что хотите зарегистрироваться?\n\nПри подтвердждении,"
    f' вы автоматически соглашаетесь с нашим <a href="{USER_AGREEMENT_URL}">'
    " пользовательских соглашением</a>."
)
