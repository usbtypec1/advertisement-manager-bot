from domain.entities.users import User
from domain.exceptions import UserNotFoundError
from infrastructure.database.dao.users import UserDAO
from infrastructure.exceptions import ObjectNotFoundError

__all__ = ("UserReadByIdInteractor",)


class UserReadByIdInteractor:
    def __init__(self, *, user_dao: UserDAO, user_id: int) -> None:
        self.__user_dao = user_dao
        self.__user_id = user_id

    def execute(self) -> User:
        try:
            user = self.__user_dao.get_by_id(self.__user_id)
        except ObjectNotFoundError:
            raise UserNotFoundError

        return User(
            id=user.id,
            full_name=user.full_name,
            username=user.username,
            created_at=user.created_at,
        )
