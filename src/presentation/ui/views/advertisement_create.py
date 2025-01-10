from collections.abc import Iterable

from aiogram.types import InputMediaPhoto, InputMediaVideo
from aiogram.utils.media_group import MediaType

from domain.entities.temporary_media_files import TemporaryMediaFile
from infrastructure.database.models import AdvertisementMediaFileType
from presentation.ui import markups, texts
from presentation.ui.views.base import MediaGroupView, PhotoView, TextView

__all__ = (
    "AdvertisementCreateTextInputView",
    "AdvertisementCreateMediaInputView",
    "AdvetisementCreateMediaUploadedView",
    "AdvertisementCreateMediaFilesView",
    "AdvertisementCreateConfirmView",
)


class AdvertisementCreateTextInputView(TextView):
    text = texts.ADVERTISEMENT_CREATE_TEXT_INPUT_TEXT
    reply_markup = markups.ADVERTISEMENT_CREATE_TEXT_INPUT_MARKUP


class AdvertisementCreateMediaInputView(TextView):
    text = texts.ADVERTISEMENT_CREATE_MEDIA_INPUT_TEXT
    reply_markup = markups.ADVERTISEMENT_CREATE_MEDIA_INPUT_MARKUP


class AdvetisementCreateMediaUploadedView(PhotoView):
    text = texts.ADVERTISEMENT_CREATE_MEDIA_UPLOADED_TEXT
    reply_markup = markups.ADVERTISEMENT_CREATE_MEDIA_UPLOADED_MARKUP


class AdvertisementCreateMediaFilesView(MediaGroupView):
    """
    View for displaying media files in the advertisement creation process.
    """

    def __init__(self, *, text: str, media_files: Iterable[TemporaryMediaFile]) -> None:
        self.__text = text
        self.__media_files = media_files

    def get_medias(self) -> list[MediaType]:
        medias: list[MediaType] = []
        for media_file in self.__media_files:
            if media_file.type == AdvertisementMediaFileType.PHOTO:
                medias.append(InputMediaPhoto(media=media_file.telegram_id))
            elif media_file.type == AdvertisementMediaFileType.VIDEO:
                medias.append(InputMediaVideo(media=media_file.telegram_id))
        return medias

    def get_caption(self) -> str:
        return self.__text


class AdvertisementCreateConfirmView(TextView):
    text = texts.ADVERTISEMENT_CREATE_CONFIRM_TEXT
    reply_markup = markups.ADVERTISEMENT_CREATE_CONFIRM_MARKUP
