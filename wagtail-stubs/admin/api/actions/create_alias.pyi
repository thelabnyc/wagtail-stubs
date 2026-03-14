from .base import APIAction as APIAction
from rest_framework.fields import BooleanField, CharField, IntegerField
from rest_framework.serializers import Serializer
from wagtail.actions.create_alias import CreatePageAliasAction as CreatePageAliasAction, CreatePageAliasIntegrityError as CreatePageAliasIntegrityError
from wagtail.api.v2.utils import BadRequestError as BadRequestError
from wagtail.models import Page as Page

class CreatePageAliasAPIActionSerializer(Serializer):
    destination_page_id: IntegerField
    recursive: BooleanField
    update_slug: CharField

class CreatePageAliasAPIAction(APIAction):
    serializer = CreatePageAliasAPIActionSerializer
    def execute(self, instance, data): ...
