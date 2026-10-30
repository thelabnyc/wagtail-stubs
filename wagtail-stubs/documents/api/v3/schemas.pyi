from typing import Any

from ninja import Schema
from wagtail.api.v3.schemas.base import BaseMetaSchema, BaseSchema
from wagtail.documents.models import AbstractDocument

Document: type[AbstractDocument]
BASE_DOCUMENT_FIELDS: list[str]

class CollectionForeignKeySchema(BaseSchema):
    id: int

class DocumentMetaSchema(BaseMetaSchema):
    detail_url: str | None = ...
    tags: list[str] = ...
    download_url: str | None = ...
    @staticmethod
    def resolve_detail_url(obj: AbstractDocument, context: dict[str, Any]) -> str | None: ...
    @staticmethod
    def resolve_tags(obj: AbstractDocument) -> list[str]: ...
    @staticmethod
    def resolve_download_url(obj: AbstractDocument, context: dict[str, Any]) -> str | None: ...

class DocumentSchema(BaseSchema):
    id: int
    title: str
    collection: CollectionForeignKeySchema
    meta: DocumentMetaSchema

def _narrowed_document_meta_schema() -> type[DocumentMetaSchema]: ...
def build_document_schemas() -> tuple[type[DocumentSchema], type[Schema], type[Schema]]: ...
