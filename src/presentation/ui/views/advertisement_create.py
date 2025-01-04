from presentation.ui import markups, texts
from presentation.ui.views.base import TextView

__all__ = ("AdvertisementCreateTextInputView",)


class AdvertisementCreateTextInputView(TextView):
    text = texts.ADVERTISEMENT_CREATE_TEXT_INPUT_TEXT
    reply_markup = markups.ADVERTISEMENT_CREATE_TEXT_INPUT_MARKUP


class AdvertisementCreatePhotoInputView(TextView):
    text = texts.ADVERTISEMENT_CREATE_PHOTO_INPUT_TEXT
    reply_markup = markups.ADVERTISEMENT_CREATE_PHOTO_INPUT_MARKUP


# class AdvetisementCreateSpecificPhotoView()
