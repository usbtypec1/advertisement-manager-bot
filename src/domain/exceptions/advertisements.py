from domain.exceptions.base import DomainFieldError

__all__ = ("AdvertisementTextLengthError",)


class AdvertisementTextLengthError(DomainFieldError):
    """Raised when advertisement text length exceeded limit."""

    def __init__(self, *, max_length: int) -> None:
        message = f"Advertisement text length exceeded limit: {max_length}"
        super().__init__(message)
        self.max_length = max_length
