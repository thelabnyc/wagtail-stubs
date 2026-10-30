from collections.abc import Callable, Iterable
from dataclasses import dataclass
from typing import Any

from django.db.models import Model
from ninja import Schema
from pydantic import BaseModel
from wagtail.admin.rich_text.converters.db_html import RichTextRemoval

class BaseMetaSchema(Schema):
    type: str
    warnings: list[RichTextRemoval | str] | None = ...
    @staticmethod
    def resolve_type(obj: Model, context: dict[str, Any]) -> str: ...
    @staticmethod
    def resolve_warnings(obj: Model, context: dict[str, Any]) -> list[str] | None: ...

class BaseSchema(Schema):
    meta: BaseMetaSchema
    @staticmethod
    def resolve_meta(obj: Model) -> Model: ...

class BaseCreateMetaSchema(Schema):
    type: str

class BaseCreateSchema(Schema):
    meta: BaseCreateMetaSchema

class BaseUpdateMetaSchema(Schema):
    type: str | None = ...

class BaseUpdateSchema(Schema):
    meta: BaseUpdateMetaSchema | None = ...

class ContentTypeSummarySchema(Schema):
    name: str
    label: str

def discriminate_meta_type(value: Any) -> str | None: ...
def build_discriminated_union(
    models: list[type[Model]],
    schema_for: Callable[[type[Model]], type[BaseModel] | None],
) -> object: ...

@dataclass(frozen=True)
class DiscriminatedUnionSchemas:
    detail: object
    create: object
    update: object

def build_union_schemas(models: Iterable[type[Model]]) -> DiscriminatedUnionSchemas: ...
