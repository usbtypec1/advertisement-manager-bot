from dataclasses import dataclass

from domain.entities.users import User
from infrastructure.database.dao.users import UserDAO

__all__ = ("UserToCreate", "UserCreateInteractor")


@dataclass(slots=True)
class UserToCreate:
    id: int
    full_name: str
    username: str | None
    phone_number: str | None


class UserCreateInteractor:
    def __init__(self, *, user_dao: UserDAO, user: UserToCreate) -> None:
        self.__user_dao = user_dao
        self.__user = user

    def execute(self) -> User:
        user = self.__user_dao.upsert(self.__user)
        return User(
            id=user.id,
            full_name=user.full_name,
            username=user.username,
            phone_number=user.phone_number,
            created_at=user.created_at,
        )
