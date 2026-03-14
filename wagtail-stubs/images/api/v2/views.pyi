from ... import get_image_model as get_image_model
from .serializers import ImageSerializer as ImageSerializer
from _typeshed import Incomplete
from wagtail.api.v2.filters import FieldsFilter as FieldsFilter, OrderingFilter as OrderingFilter, SearchFilter as SearchFilter
from wagtail.api.v2.views import BaseAPIViewSet as BaseAPIViewSet

class ImagesAPIViewSet(BaseAPIViewSet):
    base_serializer_class = ImageSerializer
    filter_backends: Incomplete
    body_fields: Incomplete
    meta_fields: Incomplete
    listing_default_fields: Incomplete
    nested_default_fields: Incomplete
    name: str
    model: Incomplete
