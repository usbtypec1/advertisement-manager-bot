import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from aiogram.fsm.storage.memory import MemoryStorage

from application.config import load_config_from_toml_file, DATABASE_FILE_PATH
from application.middlewares import DatabaseSessionMiddleware
from presentation import handlers
from infrastructure.database.models.base import Base


def include_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.include_routers(
        handlers.register.router,
        handlers.menu.router,
    )


async def main() -> None:
    config = load_config_from_toml_file()
    bot = Bot(
        token=config.telegram_bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dispatcher = Dispatcher(storage=MemoryStorage())

    include_handlers(dispatcher)

    engine = create_engine("sqlite:///" + str(DATABASE_FILE_PATH))
    session_factory = sessionmaker(engine)
    Base.metadata.create_all(engine)

    dispatcher.update.outer_middleware(DatabaseSessionMiddleware(session_factory))
    logging.basicConfig(level=logging.DEBUG)

    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
