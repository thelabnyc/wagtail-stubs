from .base import APIAction as APIAction
from _typeshed import Incomplete
from rest_framework.serializers import Serializer
from wagtail.actions.copy_page import CopyPageAction as CopyPageAction, CopyPageIntegrityError as CopyPageIntegrityError
from wagtail.api.v2.utils import BadRequestError as BadRequestError
from wagtail.coreutils import find_available_slug as find_available_slug
from wagtail.models import Page as Page

class CopyPageAPIActionSerializer(Serializer):
    destination_page_id: Incomplete
    recursive: Incomplete
    keep_live: Incomplete
    slug: Incomplete
    title: Incomplete

class CopyPageAPIAction(APIAction):
    serializer = CopyPageAPIActionSerializer
    def execute(self, instance, data): ...
