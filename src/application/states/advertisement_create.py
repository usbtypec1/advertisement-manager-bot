from aiogram.fsm.state import State, StatesGroup

__all__ = ("AdvertisementCreateStates",)


class AdvertisementCreateStates(StatesGroup):
    text = State()
    media = State()
    confirm = State()
