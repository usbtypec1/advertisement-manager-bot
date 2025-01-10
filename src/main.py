import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from application.config import DATABASE_FILE_PATH, load_config_from_toml_file
from application.middlewares import DatabaseSessionMiddleware
from infrastructure.database.models.base import Base
from presentation import handlers


def include_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.include_routers(
        handlers.advertisement_create.router,
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
