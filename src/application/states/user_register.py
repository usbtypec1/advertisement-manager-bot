from aiogram.fsm.state import State, StatesGroup


__all__ = ("UserRegisterStates",)


class UserRegisterStates(StatesGroup):
    phone_number = State()
    confirm = State()
