from domain.exceptions.base import DomainError

__all__ = ("UserNotFoundError", "UserAlreadyExistsError")


class UserNotFoundError(DomainError):
    pass


class UserAlreadyExistsError(DomainError):
    pass
