from ... import get_document_model as get_document_model
from .serializers import DocumentSerializer as DocumentSerializer
from _typeshed import Incomplete
from wagtail.api.v2.filters import FieldsFilter as FieldsFilter, OrderingFilter as OrderingFilter, SearchFilter as SearchFilter
from wagtail.api.v2.views import BaseAPIViewSet as BaseAPIViewSet

class DocumentsAPIViewSet(BaseAPIViewSet):
    base_serializer_class = DocumentSerializer
    filter_backends: Incomplete
    body_fields: Incomplete
    meta_fields: Incomplete
    listing_default_fields: Incomplete
    nested_default_fields: Incomplete
    name: str
    model: Incomplete
