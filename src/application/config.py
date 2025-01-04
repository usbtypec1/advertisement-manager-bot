import pathlib
from dataclasses import dataclass
from typing import Final

import tomllib

__all__ = (
    "Config",
    "load_config_from_toml_file",
    "CONFIG_FILE_PATH",
    "DATABASE_FILE_PATH",
)


CONFIG_FILE_PATH: Final[pathlib.Path] = (
    pathlib.Path(__file__).parent.parent.parent / "config.toml"
)
DATABASE_FILE_PATH: Final[pathlib.Path] = (
    pathlib.Path(__file__).parent.parent.parent / "database.db"
)


@dataclass(frozen=True, slots=True)
class Config:
    telegram_bot_token: str
    moderation_chat_id: int


def load_config_from_toml_file(
    file_path: pathlib.Path = CONFIG_FILE_PATH,
) -> Config:
    config_toml = file_path.read_text(encoding="utf-8")
    config = tomllib.loads(config_toml)
    return Config(
        telegram_bot_token=config["telegram_bot"]["token"],
        moderation_chat_id=config["moderation"]["chat_id"],
    )
