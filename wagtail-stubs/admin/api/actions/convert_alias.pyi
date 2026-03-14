from .base import APIAction as APIAction
from rest_framework.serializers import Serializer
from wagtail.actions.convert_alias import ConvertAliasPageAction as ConvertAliasPageAction, ConvertAliasPageError as ConvertAliasPageError
from wagtail.api.v2.utils import BadRequestError as BadRequestError

class ConvertAliasPageAPIAction(APIAction):
    serializer = Serializer
    def execute(self, instance, data): ...
