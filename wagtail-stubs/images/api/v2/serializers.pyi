from _typeshed import Incomplete
from rest_framework.fields import Field
from wagtail.api.v2.serializers import BaseSerializer as BaseSerializer

class ImageDownloadUrlField(Field):
    def get_attribute(self, instance): ...
    def to_representation(self, image): ...

class ImageSerializer(BaseSerializer):
    download_url: Incomplete
