from .base import APIAction as APIAction
from rest_framework.fields import BooleanField, CharField, IntegerField
from rest_framework.serializers import Serializer
from wagtail.actions.copy_page import CopyPageAction as CopyPageAction, CopyPageIntegrityError as CopyPageIntegrityError
from wagtail.api.v2.utils import BadRequestError as BadRequestError
from wagtail.coreutils import find_available_slug as find_available_slug
from wagtail.models import Page as Page

class CopyPageAPIActionSerializer(Serializer):
    destination_page_id: IntegerField
    recursive: BooleanField
    keep_live: BooleanField
    slug: CharField
    title: CharField

class CopyPageAPIAction(APIAction):
    serializer = CopyPageAPIActionSerializer
    def execute(self, instance, data): ...
