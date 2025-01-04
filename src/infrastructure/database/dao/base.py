from sqlalchemy.orm import Session

__all__ = ("DatabaseDAO",)


class DatabaseDAO:
    def __init__(self, session: Session) -> None:
        self._session = session
