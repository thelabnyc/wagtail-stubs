from datetime import datetime
from typing import Any, ClassVar, Literal

from django.db.models import Model
from django.http import HttpRequest
from ninja import NinjaAPI
from ninja.types import DictStrAny
from wagtail.api.v3.schemas.base import (
    BaseCreateMetaSchema,
    BaseCreateSchema,
    BaseMetaSchema,
    BaseSchema,
    BaseUpdateMetaSchema,
    BaseUpdateSchema,
)
from wagtail.api.v3.schemas.params import TypeInjectingBody, TypeInjectingBodyModel
from wagtail.models import AbstractPage

Page: type[AbstractPage]
BASE_PAGE_FIELDS: list[str]
field: str
BASE_PAGE_READ_FIELDS: list[str]
BASE_PAGE_READ_FIELDS_SET: set[str]

class SimpleBasePageMetaSchema(BaseMetaSchema):
    type: str | None = ...  # type: ignore[assignment]
    detail_url: str | None = ...
    html_url: str | None = ...
    @staticmethod
    def resolve_type(obj: Model, context: dict[str, Any]) -> str: ...
    @staticmethod
    def resolve_detail_url(obj: AbstractPage, context: dict[str, Any]) -> str | None: ...
    @staticmethod
    def resolve_html_url(obj: AbstractPage, context: dict[str, Any]) -> str | None: ...

class SimpleBasePageSchema(BaseSchema):
    id: int
    title: str
    meta: SimpleBasePageMetaSchema

class BasePageMetaSchema(SimpleBasePageMetaSchema):
    locale: str | None = ...
    slug: str
    first_published_at: datetime | None = ...
    @staticmethod
    def resolve_locale(obj: AbstractPage, context: dict[str, Any]) -> str | None: ...

class BasePageSchema(SimpleBasePageSchema):
    meta: BasePageMetaSchema

class PageMetaSchema(BasePageMetaSchema):
    show_in_menus: bool | None = ...
    seo_title: str | None = ...
    search_description: str | None = ...
    alias_of: SimpleBasePageSchema | None = ...
    parent: SimpleBasePageSchema | None = ...
    @staticmethod
    def resolve_parent(obj: AbstractPage, context: dict[str, Any]) -> AbstractPage | None: ...

class PageSchema(BasePageSchema):
    meta: PageMetaSchema

class PageCreateMetaSchema(BaseCreateMetaSchema):
    parent_id: int
    action: Literal["publish"] | None = ...

class PageCreateBaseSchema(BaseCreateSchema):
    meta: PageCreateMetaSchema

class PageUpdateMetaSchema(BaseUpdateMetaSchema):
    action: Literal["publish"] | None = ...

class PageUpdateBaseSchema(BaseUpdateSchema):
    meta: PageUpdateMetaSchema | None = ...

class PageTypeInjectingBodyModel(TypeInjectingBodyModel):
    page_id_param: ClassVar[str]
    @classmethod
    def get_meta_type(cls, request: HttpRequest, api: NinjaAPI, path_params: DictStrAny) -> str: ...

class PageTypeInjectingBody(TypeInjectingBody):  # type: ignore[misc]
    _model: type[PageTypeInjectingBodyModel]
