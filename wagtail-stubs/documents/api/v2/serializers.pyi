from _typeshed import Incomplete
from rest_framework.fields import Field
from wagtail.api.v2.serializers import BaseSerializer as BaseSerializer
from wagtail.api.v2.utils import get_full_url as get_full_url

class DocumentDownloadUrlField(Field):
    def get_attribute(self, instance): ...
    def to_representation(self, document): ...

class DocumentSerializer(BaseSerializer):
    download_url: Incomplete
