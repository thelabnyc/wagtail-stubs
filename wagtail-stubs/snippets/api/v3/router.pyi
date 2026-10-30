from collections.abc import Callable
from typing import Any, Literal, TypeAlias

from django.db.models import Model
from django.http import HttpRequest
from ninja import Router, Schema, Status
from ninja.params.models import Body as _BodyParam
from ninja.params.models import Query as _QueryParam
from pydantic import BaseModel
from wagtail.api.rich_text import RichTextOutputFormat
from wagtail.api.v3.schemas.params import (
    OrderingSchema,
    RevisionFilterSchema,
    SearchSchema,
    TranslationFilterSchema,
)
from wagtail.api.v3.schemas.revisions import RevisionDetailSchema
from wagtail.models import DraftStateMixin, Revision, RevisionMixin, TranslatableMixin

router: Router
actions_router: Router
enabled_models: list[type[Model]]
SnippetTypeLiteral: TypeAlias = str  # NOQA:UP040
SnippetDetailSchema: object
SnippetCreateSchema: object
SnippetUpdateSchema: object
mixins: tuple[type[RevisionMixin], type[DraftStateMixin], type[TranslatableMixin]]
literals_by_mixin: dict[type[Model], object]
schemas_by_mixin: dict[type[Model], object]
mixin: type[RevisionMixin | DraftStateMixin | TranslatableMixin]
models: list[type[Model]]
for_schema: Callable[[type[Model]], type[BaseModel] | None]

def get_model_from_params(request: HttpRequest, *args: Any, type: SnippetTypeLiteral, **kwargs: Any) -> type[Model]: ...
def _check_can_view_revisions(request: HttpRequest, instance: Model) -> None: ...

class SnippetRevisionDetailSchema(RevisionDetailSchema):
    content_object: object
    @staticmethod
    def resolve_content_object(obj: Revision) -> Model: ...

def list_snippets(
    request: HttpRequest,
    type: SnippetTypeLiteral,
    translation_filter: TranslationFilterSchema | _QueryParam = ...,
    ordering: OrderingSchema | _QueryParam = ...,
    search: SearchSchema | _QueryParam = ...,
    rich_text_format: RichTextOutputFormat | _QueryParam | None = ...,
    **kwargs: Any,
) -> dict[str, Any]: ...
def get_snippet(
    request: HttpRequest,
    type: SnippetTypeLiteral,
    pk: str,
    version: Literal["live", "draft"] | _QueryParam = ...,
    rich_text_format: RichTextOutputFormat | _QueryParam | None = ...,
) -> Model: ...
def create_snippet(
    request: HttpRequest,
    type: SnippetTypeLiteral,
    data: BaseModel | _BodyParam = ...,
    rich_text_format: RichTextOutputFormat | _QueryParam | None = ...,
) -> Status[Model]: ...
def update_snippet(
    request: HttpRequest,
    type: SnippetTypeLiteral,
    pk: str,
    data: BaseModel | _BodyParam = ...,
    rich_text_format: RichTextOutputFormat | _QueryParam | None = ...,
) -> Model: ...
def delete_snippet(request: HttpRequest, type: SnippetTypeLiteral, pk: str) -> Status[None]: ...
def list_snippet_revisions(
    request: HttpRequest,
    type: SnippetTypeLiteral,
    pk: str,
    filters: RevisionFilterSchema | _QueryParam = ...,
) -> dict[str, Any]: ...
def get_snippet_revision(request: HttpRequest, type: SnippetTypeLiteral, pk: str, revision_id: int) -> Revision: ...
def publish_snippet(request: HttpRequest, type: SnippetTypeLiteral, pk: str) -> Model: ...
def unpublish_snippet(request: HttpRequest, type: SnippetTypeLiteral, pk: str) -> Model: ...

class SnippetRevertSchema(Schema):
    revision_id: int

def revert_snippet(
    request: HttpRequest, type: SnippetTypeLiteral, pk: str, data: SnippetRevertSchema | _BodyParam = ...
) -> Model: ...

class SnippetCopyForTranslationSchema(Schema):
    locale: str

def copy_for_translation(
    request: HttpRequest, type: SnippetTypeLiteral, pk: str, data: SnippetCopyForTranslationSchema | _BodyParam = ...
) -> Status[Model]: ...
