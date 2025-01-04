from collections.abc import Generator
import sqlite3
import pathlib
from typing import Final


__all__ = ("get_connection", "DATABASE_FILE_PATH")


DATABASE_FILE_PATH: Final[pathlib.Path] = (
    pathlib.Path(__file__).parent.parent.parent / "database.db"
)


def get_connection() -> Generator[sqlite3.Connection, None, None]:
    with sqlite3.connect(DATABASE_FILE_PATH) as connection:
        yield connection
