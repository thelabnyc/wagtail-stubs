from .base import APIAction as APIAction
from rest_framework.fields import IntegerField
from rest_framework.serializers import Serializer
from wagtail.actions.revert_to_page_revision import RevertToPageRevisionAction as RevertToPageRevisionAction, RevertToPageRevisionError as RevertToPageRevisionError
from wagtail.api.v2.utils import BadRequestError as BadRequestError

class RevertToPageRevisionAPIActionSerializer(Serializer):
    revision_id: IntegerField

class RevertToPageRevisionAPIAction(APIAction):
    serializer = RevertToPageRevisionAPIActionSerializer
    def execute(self, instance, data): ...
