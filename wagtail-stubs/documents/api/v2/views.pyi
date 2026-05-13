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
from wagtail.documents.models import AbstractDocument

from ... import get_document_model as get_document_model
from .serializers import DocumentSerializer as DocumentSerializer

class DocumentsAPIViewSet(BaseAPIViewSet):
    base_serializer_class = DocumentSerializer
    filter_backends: list[type[FieldsFilter | OrderingFilter | SearchFilter]]
    body_fields: list[str]
    meta_fields: list[str]
    listing_default_fields: list[str]
    nested_default_fields: list[str]
    name: str
    model: type[AbstractDocument]
    def get_queryset(self) -> QuerySet[AbstractDocument]: ...
