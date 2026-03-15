from django.db import models
from rest_framework.fields import Field
from wagtail.api.v2.serializers import BaseSerializer as BaseSerializer
from wagtail.api.v2.utils import get_full_url as get_full_url

class DocumentDownloadUrlField(Field):
    def get_attribute(self, instance: models.Model) -> models.Model: ...
    def to_representation(self, document: models.Model) -> str: ...

class DocumentSerializer(BaseSerializer):
    download_url: DocumentDownloadUrlField
