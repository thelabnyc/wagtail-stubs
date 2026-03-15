from rest_framework.fields import BooleanField
from rest_framework.serializers import Serializer
from wagtail.actions.unpublish_page import UnpublishPageAction as UnpublishPageAction

from .base import APIAction as APIAction

class UnpublishPageAPIActionSerializer(Serializer):
    recursive: BooleanField

class UnpublishPageAPIAction(APIAction):
    serializer = UnpublishPageAPIActionSerializer
    def execute(self, instance, data): ...
