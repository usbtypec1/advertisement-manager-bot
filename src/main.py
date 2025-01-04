import asyncio

from aiogram import Bot, Dispatcher
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from application.config import load_config_from_toml_file, DATABASE_FILE_PATH
from application.middlewares import DatabaseSessionMiddleware


async def main() -> None:
    config = load_config_from_toml_file()
    bot = Bot(token=config.telegram_bot_token)
    dispatcher = Dispatcher()

    engine = create_engine("sqlite:///" + str(DATABASE_FILE_PATH))
    session_factory = sessionmaker(engine)

    dispatcher.update.middleware(DatabaseSessionMiddleware(session_factory))

    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
