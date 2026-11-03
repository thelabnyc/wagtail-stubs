from typing import Any

from ninja import Schema
from wagtail.models import AbstractPage

Page: type[AbstractPage]

class AdminSimplePageMetaSchema(Schema):
    type: str
    @staticmethod
    def resolve_type(obj: AbstractPage) -> str: ...

class AdminSimplePageSchema(Schema):
    id: int
    title: str
    meta: AdminSimplePageMetaSchema
    @staticmethod
    def resolve_meta(obj: AbstractPage) -> AbstractPage: ...

class AdminPageMetaSchema(AdminSimplePageMetaSchema):
    locale: str
    depth: int
    status: str
    live: bool
    has_unpublished_changes: bool
    has_children: bool
    @staticmethod
    def resolve_locale(obj: AbstractPage) -> str: ...
    @staticmethod
    def resolve_status(obj: AbstractPage) -> str: ...
    @staticmethod
    def resolve_has_children(obj: AbstractPage) -> bool: ...

class AdminPageDetailMetaSchema(AdminPageMetaSchema):
    parent: AdminSimplePageSchema | None = ...
    @staticmethod
    def resolve_parent(obj: AbstractPage, context: dict[str, Any]) -> AbstractPage | None: ...

class AdminPageSchema(AdminSimplePageSchema):
    meta: AdminPageMetaSchema
    admin_display_title: str
    @staticmethod
    def resolve_admin_display_title(obj: AbstractPage) -> str: ...

class AdminPageDetailSchema(AdminPageSchema):
    meta: AdminPageDetailMetaSchema

class ExplorerTranslationSchema(Schema):
    id: int
    locale: str
    @staticmethod
    def resolve_locale(obj: AbstractPage) -> str: ...

class ExplorerChildrenSchema(Schema):
    count: int
    items: list[AdminPageSchema]

class ExplorerSchema(Schema):
    page: AdminPageDetailSchema
    translations: list[ExplorerTranslationSchema]
    children: ExplorerChildrenSchema
