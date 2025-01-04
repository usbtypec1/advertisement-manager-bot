from dataclasses import dataclass
from datetime import datetime
from typing import Protocol

from sqlalchemy import select

from infrastructure.database.dao.base import DatabaseDAO
from infrastructure.database.models import User
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
    phone_number: str | None


class UserDAO(DatabaseDAO):
    def upsert(self, user: UserCreate) -> UserDTO:
        user_to_create = User(
            id=user.id,
            full_name=user.full_name,
            username=user.username,
            phone_number=user.phone_number,
        )

        with self._session.begin():
            user_created = self._session.merge(user_to_create)

        return UserDTO(
            id=user_created.id,
            full_name=user_created.full_name,
            username=user_created.username,
            phone_number=user_created.phone_number,
            created_at=user_created.created_at,
        )

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
