from .base import APIAction as APIAction
from rest_framework.serializers import Serializer
from wagtail.actions.publish_page_revision import PublishPageRevisionAction as PublishPageRevisionAction
from wagtail.api.v2.utils import BadRequestError as BadRequestError

class PublishPageAPIAction(APIAction):
    serializer = Serializer
    def execute(self, instance, data): ...
