from .base import APIAction as APIAction
from rest_framework.serializers import Serializer
from wagtail.actions.delete_page import DeletePageAction as DeletePageAction

class DeletePageAPIAction(APIAction):
    serializer = Serializer
    def execute(self, instance, data): ...
