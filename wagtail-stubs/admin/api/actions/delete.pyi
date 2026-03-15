from rest_framework.serializers import Serializer
from wagtail.actions.delete_page import DeletePageAction as DeletePageAction

from .base import APIAction as APIAction

class DeletePageAPIAction(APIAction):
    serializer = Serializer
    def execute(self, instance, data): ...
