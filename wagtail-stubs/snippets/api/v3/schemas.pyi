from typing import Any, ClassVar

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

class SnippetMetaSchema(BaseMetaSchema):
    detail_url: str | None = ...
    @staticmethod
    def resolve_detail_url(obj: Model, context: dict[str, Any]) -> str | None: ...

class BaseSnippetSchema(BaseSchema):
    meta: SnippetMetaSchema

class BaseSnippetCreateMetaSchema(BaseCreateMetaSchema):
    type: str | None = ...  # type: ignore[assignment]

class BaseSnippetCreateSchema(BaseCreateSchema):
    meta: BaseSnippetCreateMetaSchema | None = ...  # type: ignore[assignment]

class BaseSnippetUpdateMetaSchema(BaseUpdateMetaSchema): ...

class BaseSnippetUpdateSchema(BaseUpdateSchema):
    meta: BaseSnippetUpdateMetaSchema | None = ...

PUBLISH_ACTION_META_FIELD: dict[str, tuple[Any, Any]]

class ParamTypeInjectingBodyModel(TypeInjectingBodyModel):
    type_param: ClassVar[str]
    @classmethod
    def get_meta_type(cls, request: HttpRequest, api: NinjaAPI, path_params: DictStrAny) -> str: ...

class ParamTypeInjectingBody(TypeInjectingBody):  # type: ignore[misc]
    _model: type[ParamTypeInjectingBodyModel]
