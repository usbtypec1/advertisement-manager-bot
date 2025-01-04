from presentation.ui import markups, texts
from presentation.ui.views.base import PhotoView, TextView

__all__ = (
    "AdvertisementCreateTextInputView",
    "AdvertisementCreateMediaInputView",
    "AdvetisementCreateMediaUploadedView",
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
