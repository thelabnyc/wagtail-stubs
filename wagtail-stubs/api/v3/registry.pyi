from dataclasses import dataclass
from typing import Any, TypedDict

from pydantic import BaseModel
from wagtail.api.v3.schemas import ContentTypeSummarySchema

@dataclass
class ContentTypeRegistration:
    name: str
    label: str
    read_schema: type[BaseModel] | None = None
    create_schema: type[BaseModel] | None = None
    patch_schema: type[BaseModel] | None = None

class _TypeSchemas(TypedDict):
    read: dict[str, Any]
    create: dict[str, Any]
    patch: dict[str, Any]

class ContentTypeRegistry:
    def __init__(self) -> None: ...
    def register(self, registration: ContentTypeRegistration) -> None: ...
    def list_content_types(self) -> list[ContentTypeSummarySchema]: ...
    def has(self, name: str) -> bool: ...
    def get(self, name: str) -> ContentTypeRegistration | None: ...
    def get_type_schemas(self, name: str) -> _TypeSchemas | None: ...
    def register_defaults(self) -> None: ...
    def _schema_for_direction(self, registration: ContentTypeRegistration, direction: str) -> dict[str, Any] | None: ...

registry: ContentTypeRegistry
