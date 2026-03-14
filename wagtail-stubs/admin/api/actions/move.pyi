from .base import APIAction as APIAction
from _typeshed import Incomplete
from rest_framework.serializers import Serializer
from wagtail.actions.move_page import MovePageAction as MovePageAction
from wagtail.models import Page as Page

class MovePageAPIActionSerializer(Serializer):
    destination_page_id: Incomplete
    position: Incomplete

class MovePageAPIAction(APIAction):
    serializer = MovePageAPIActionSerializer
    def execute(self, instance, data): ...
