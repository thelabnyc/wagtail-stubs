from rest_framework.fields import Field
from wagtail.api.v2.serializers import BaseSerializer as BaseSerializer
from wagtail.images.models import AbstractImage

class ImageDownloadUrlField(Field):
    def get_attribute(self, instance: AbstractImage) -> AbstractImage: ...
    def to_representation(self, image: AbstractImage) -> str: ...

class ImageSerializer(BaseSerializer):
    download_url: ImageDownloadUrlField
