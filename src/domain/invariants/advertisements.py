from typing import Final

from domain.exceptions import AdvertisementTextLengthError

__all__ = (
    "ADVERTISEMENT_TEXT_MAX_LENGTH",
    "validate_advertisement_text_length",
)


ADVERTISEMENT_TEXT_MAX_LENGTH: Final[int] = 1024


def validate_advertisement_text_length(text: str) -> None:
    if len(text) > ADVERTISEMENT_TEXT_MAX_LENGTH:
        raise AdvertisementTextLengthError(
            max_length=ADVERTISEMENT_TEXT_MAX_LENGTH,
        )
