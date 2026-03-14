from .base import APIAction as APIAction
from _typeshed import Incomplete
from rest_framework.serializers import Serializer
from wagtail.actions.unpublish_page import UnpublishPageAction as UnpublishPageAction

class UnpublishPageAPIActionSerializer(Serializer):
    recursive: Incomplete

class UnpublishPageAPIAction(APIAction):
    serializer = UnpublishPageAPIActionSerializer
    def execute(self, instance, data): ...
