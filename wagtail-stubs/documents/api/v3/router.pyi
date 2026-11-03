from typing import Any

from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import Router, Schema, Status, UploadedFile
from ninja.params.models import Body as _BodyParam
from ninja.params.models import File as _FileParam
from ninja.params.models import Form as _FormParam
from ninja.params.models import Query as _QueryParam
from pydantic import BaseModel
from wagtail.api.v3.pagination import WagtailLimitOffsetPagination
from wagtail.api.v3.registry import ContentTypeRegistration
from wagtail.api.v3.schemas.params import OrderingSchema, SearchSchema
from wagtail.documents.api.v3.schemas import DocumentSchema
from wagtail.documents.models import AbstractDocument

router: Router
Document: type[AbstractDocument]
registered_schemas: ContentTypeRegistration

class DocumentDetailSchema(DocumentSchema): ...
class DocumentCreateSchema(Schema): ...
class DocumentPatchSchema(Schema): ...

BASE_DOCUMENT_READ_FIELDS: list[str]

def get_documents_queryset(request: HttpRequest) -> QuerySet[AbstractDocument]: ...
def list_documents(
    request: HttpRequest,
    *,
    ordering: OrderingSchema | _QueryParam = ...,
    search: SearchSchema | _QueryParam = ...,
    ninja_pagination: WagtailLimitOffsetPagination.Input | None = None,
    **kwargs: Any,
) -> dict[str, Any]: ...
def get_document(request: HttpRequest, document_id: int) -> AbstractDocument: ...
def create_document(
    request: HttpRequest, file: UploadedFile | _FileParam = ..., data: BaseModel | _FormParam = ...
) -> Status[AbstractDocument]: ...
def update_document(request: HttpRequest, document_id: int, data: BaseModel | _BodyParam = ...) -> AbstractDocument: ...
def delete_document(request: HttpRequest, document_id: int) -> Status[None]: ...
