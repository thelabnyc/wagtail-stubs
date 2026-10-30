from collections.abc import Callable, Iterable
from types import UnionType
from typing import Any, TypeAlias

from django.db.models import ForeignKey, ForeignObjectRel, Model
from django.db.models.fields import Field
from ninja import Schema
from pydantic import BaseModel
from wagtail.admin.rich_text.converters.db_html import RichTextRemoval
from wagtail.api.rich_text import RichTextInputFormat
from wagtail.fields import RichTextField

InputFieldSchema: TypeAlias = tuple[Any, Any] | None  # NOQA:UP040
InputFieldSchemaFunc: TypeAlias = Callable[[InputSchemaGenerator, Field[Any, Any]], InputFieldSchema]  # NOQA:UP040

class InputSchemaGenerator:
    for_update: bool
    name_suffix: str
    field_schemas: dict[type[Field[Any, Any] | ForeignObjectRel], InputFieldSchemaFunc]
    def __init__(self, *, for_update: bool = False) -> None: ...
    def register_field_schema[F: Field[Any, Any] | ForeignObjectRel](
        self,
        field_class: type[F],
        func: Callable[[InputSchemaGenerator, F], InputFieldSchema],
    ) -> None: ...
    def get_child_relation_schema(self, model: type[Model]) -> type[Schema]: ...
    def _build_extra_fields(self, model: type[Model]) -> dict[str, tuple[Any, Any]]: ...
    @staticmethod
    def _is_optional(annotation: type[Any] | UnionType) -> bool: ...
    @staticmethod
    def _narrowed_meta_schema(
        base_meta_schema: type[Any] | UnionType,
        model: type[Model],
        name_suffix: str,
        extra_fields: dict[str, tuple[Any, Any]] | None = None,
    ) -> type[Schema] | UnionType: ...
    @staticmethod
    def _make_optional(field_schema: tuple[Any, Any]) -> tuple[Any, Any]: ...
    def generate_schema[S: Schema](
        self,
        model: type[Model],
        *,
        base_class: type[S],
        fields: Iterable[str] = (),
        required_fields: Iterable[str] = (),
        extra_meta_fields: dict[str, tuple[Any, Any]] | None = None,
    ) -> type[S]: ...

class RichTextInputSchema(BaseModel):
    format: RichTextInputFormat = ...
    content: str
    removals: list[RichTextRemoval] = ...

def rich_text_schema(generator: InputSchemaGenerator, field: RichTextField) -> InputFieldSchema: ...
def streamfield_schema(generator: InputSchemaGenerator, field: Field[Any, Any]) -> InputFieldSchema: ...
def tags_schema(generator: InputSchemaGenerator, field: Field[Any, Any]) -> InputFieldSchema: ...
def child_relation_schema(generator: InputSchemaGenerator, field: ForeignObjectRel) -> InputFieldSchema: ...
def foreign_key_schema(generator: InputSchemaGenerator, field: ForeignKey[Any, Any]) -> InputFieldSchema: ...
def register_default_field_schemas(generator: InputSchemaGenerator) -> None: ...

create_generator: InputSchemaGenerator
patch_generator: InputSchemaGenerator
