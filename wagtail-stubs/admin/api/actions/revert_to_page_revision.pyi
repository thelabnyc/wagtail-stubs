from .base import APIAction as APIAction
from _typeshed import Incomplete
from rest_framework.serializers import Serializer
from wagtail.actions.revert_to_page_revision import RevertToPageRevisionAction as RevertToPageRevisionAction, RevertToPageRevisionError as RevertToPageRevisionError
from wagtail.api.v2.utils import BadRequestError as BadRequestError

class RevertToPageRevisionAPIActionSerializer(Serializer):
    revision_id: Incomplete

class RevertToPageRevisionAPIAction(APIAction):
    serializer = RevertToPageRevisionAPIActionSerializer
    def execute(self, instance, data): ...
