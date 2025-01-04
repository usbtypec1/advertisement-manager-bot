from datetime import datetime
from typing import Protocol
from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.dialects.sqlite import insert

from infrastructure.database.models import User
from infrastructure.database.dao.base import DatabaseDAO
from infrastructure.exceptions import ObjectNotFoundError


__all__ = ("UserDAO",)


@dataclass(frozen=True, slots=True)
class UserDTO:
    id: int
    full_name: str
    username: str | None
    phone_number: str | None
    created_at: datetime


class UserCreate(Protocol):
    id: int
    full_name: str
    username: str | None


class UserDAO(DatabaseDAO):
    def upsert(self, user: UserCreate) -> None:
        statement = insert(User).values(
            id=user.id, full_name=user.full_name, username=user.username
        )
        statement = statement.on_conflict_do_update(
            index_elements=(User.id,),
            set_={"full_name": user.full_name, "username": user.username},
        )
        with self._session.begin():
            self._session.execute(statement)

    def get_by_id(self, user_id: int) -> UserDTO:
        statement = select(User).where(User.id == user_id)
        user: User | None = self._session.scalar(statement)
        if user is None:
            raise ObjectNotFoundError(f"User by id {user_id} does not exist")
        return UserDTO(
            id=user.id,
            full_name=user.full_name,
            username=user.username,
            phone_number=user.phone_number,
            created_at=user.created_at,
        )
