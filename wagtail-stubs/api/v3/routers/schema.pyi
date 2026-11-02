from typing import Any

from django.http import HttpRequest
from ninja import Router, Schema
from wagtail.api.v3.registry import _TypeSchemas
from wagtail.api.v3.schemas import ContentTypeSummarySchema

router: Router

class ContentTypeListSchema(Schema):
    types: list[ContentTypeSummarySchema]

class SchemaDetailResponse(Schema):
    read: dict[str, Any] | None = ...
    create: dict[str, Any] | None = ...
    patch: dict[str, Any] | None = ...

def list_schemas(request: HttpRequest) -> dict[str, list[ContentTypeSummarySchema]]: ...
def get_schema_for_type(request: HttpRequest, type_name: str) -> _TypeSchemas: ...
