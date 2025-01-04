from domain.exceptions.base import DomainFieldError

__all__ = ("AdvertisementTextLengthError",)


class AdvertisementTextLengthError(DomainFieldError):
    """Raised when advertisement text length exceeded limit."""
