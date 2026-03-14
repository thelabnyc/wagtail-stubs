from .base import APIAction as APIAction
from rest_framework.fields import BooleanField, CharField
from rest_framework.serializers import Serializer
from wagtail.actions.copy_for_translation import CopyPageForTranslationAction as CopyPageForTranslationAction, ParentNotTranslatedError as ParentNotTranslatedError
from wagtail.api.v2.utils import BadRequestError as BadRequestError
from wagtail.models.i18n import Locale as Locale

class CopyForTranslationAPIActionSerializer(Serializer):
    locale: CharField
    copy_parents: BooleanField
    alias: BooleanField
    recursive: BooleanField

class CopyForTranslationAPIAction(APIAction):
    serializer = CopyForTranslationAPIActionSerializer
    def execute(self, instance, data): ...
