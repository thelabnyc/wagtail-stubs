from ... import get_image_model as get_image_model
from .serializers import ImageSerializer as ImageSerializer
from django.db import models
from wagtail.api.v2.filters import FieldsFilter as FieldsFilter, OrderingFilter as OrderingFilter, SearchFilter as SearchFilter
from wagtail.api.v2.views import BaseAPIViewSet as BaseAPIViewSet

class ImagesAPIViewSet(BaseAPIViewSet):
    base_serializer_class = ImageSerializer
    filter_backends: list[type[FieldsFilter | OrderingFilter | SearchFilter]]
    body_fields: list[str]
    meta_fields: list[str]
    listing_default_fields: list[str]
    nested_default_fields: list[str]
    name: str
    model: type[models.Model]
