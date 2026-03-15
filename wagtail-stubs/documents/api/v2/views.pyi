from django.db import models

from ... import get_document_model as get_document_model
from .serializers import DocumentSerializer as DocumentSerializer
from wagtail.api.v2.filters import FieldsFilter as FieldsFilter, OrderingFilter as OrderingFilter, SearchFilter as SearchFilter
from wagtail.api.v2.views import BaseAPIViewSet as BaseAPIViewSet

class DocumentsAPIViewSet(BaseAPIViewSet):
    base_serializer_class = DocumentSerializer
    filter_backends: list[type]
    body_fields: list[str]
    meta_fields: list[str]
    listing_default_fields: list[str]
    nested_default_fields: list[str]
    name: str
    model: type[models.Model]
