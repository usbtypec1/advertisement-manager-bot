from collections.abc import Callable, Awaitable
from typing import Any

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.orm import sessionmaker


__all__ = ("DatabaseSessionMiddleware",)


class DatabaseSessionMiddleware(BaseMiddleware):
    def __init__(self, session_factory: sessionmaker) -> None:
        self.__session_factory = session_factory

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        async with self.__session_factory() as session:
            data["session"] = session
            return await super().__call__(handler, event, data)
