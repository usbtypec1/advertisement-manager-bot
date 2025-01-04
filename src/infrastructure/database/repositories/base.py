from sqlalchemy.orm import Session


__all__ = ("DatabaseRepository",)


class DatabaseRepository:
    def __init__(self, session: Session) -> None:
        self._session = session
