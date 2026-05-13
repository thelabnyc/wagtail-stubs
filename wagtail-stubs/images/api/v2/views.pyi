from django.db.models import QuerySet
from wagtail.api.v2.filters import (
    FieldsFilter as FieldsFilter,
)
from wagtail.api.v2.filters import (
    OrderingFilter as OrderingFilter,
)
from wagtail.api.v2.filters import (
    SearchFilter as SearchFilter,
)
from wagtail.api.v2.views import BaseAPIViewSet as BaseAPIViewSet
from wagtail.images.models import AbstractImage

from ... import get_image_model as get_image_model
from .serializers import ImageSerializer as ImageSerializer

class ImagesAPIViewSet(BaseAPIViewSet):
    base_serializer_class = ImageSerializer
    filter_backends: list[type[FieldsFilter | OrderingFilter | SearchFilter]]
    body_fields: list[str]
    meta_fields: list[str]
    listing_default_fields: list[str]
    nested_default_fields: list[str]
    name: str
    model: type[AbstractImage]
    def get_queryset(self) -> QuerySet[AbstractImage]: ...
