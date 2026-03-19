from typing import Any

from django.db.models import QuerySet
from django.utils.functional import classproperty
from rest_framework.filters import BaseFilterBackend
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from wagtail.api import APIField as APIField
from wagtail.models.pages import Page as Page
from wagtail.models.pages import PageViewRestriction as PageViewRestriction
from wagtail.models.sites import Site as Site

from .filters import (
    AncestorOfFilter as AncestorOfFilter,
)
from .filters import (
    ChildOfFilter as ChildOfFilter,
)
from .filters import (
    DescendantOfFilter as DescendantOfFilter,
)
from .filters import (
    FieldsFilter as FieldsFilter,
)
from .filters import (
    LocaleFilter as LocaleFilter,
)
from .filters import (
    OrderingFilter as OrderingFilter,
)
from .filters import (
    SearchFilter as SearchFilter,
)
from .filters import (
    TranslationOfFilter as TranslationOfFilter,
)
from .pagination import WagtailPagination as WagtailPagination
from .serializers import (
    BaseSerializer as BaseSerializer,
)
from .serializers import (
    PageSerializer as PageSerializer,
)
from .serializers import (
    get_serializer_class as get_serializer_class,
)
from .utils import (
    BadRequestError as BadRequestError,
)
from .utils import (
    get_object_detail_url as get_object_detail_url,
)
from .utils import (
    page_models_from_string as page_models_from_string,
)
from .utils import (
    parse_fields_parameter as parse_fields_parameter,
)

class BaseAPIViewSet(GenericViewSet):
    @classproperty
    def renderer_classes(cls) -> list[type]: ...
    pagination_class: type[WagtailPagination]
    base_serializer_class: type[BaseSerializer]
    filter_backends: list[type[BaseFilterBackend]]
    model: type | None
    known_query_parameters: frozenset[str]
    find_query_parameters: list[str]
    body_fields: list[str]
    meta_fields: list[str]
    listing_default_fields: list[str]
    nested_default_fields: list[str]
    detail_only_fields: list[str]
    name: str | None
    seen_types: dict[str, type]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_queryset(self) -> QuerySet[Any]: ...
    def listing_view(self, request: Request) -> Response: ...
    def detail_view(self, request: Request, pk: Any) -> Response: ...
    def find_view(self, request: Request) -> Response: ...
    def find_object(self, queryset: QuerySet[Any], request: Request) -> Any: ...
    def handle_exception(self, exc: Exception) -> Response: ...
    @classmethod
    def get_body_fields(cls, model: type) -> list[str]: ...
    @classmethod
    def get_body_fields_names(cls, model: type) -> list[str]: ...
    @classmethod
    def get_meta_fields(cls, model: type) -> list[str]: ...
    @classmethod
    def get_meta_fields_names(cls, model: type) -> list[str]: ...
    @classmethod
    def get_field_serializer_overrides(cls, model: type) -> dict[str, Any]: ...
    @classmethod
    def get_available_fields(cls, model: type, db_fields_only: bool = False) -> list[str]: ...
    @classmethod
    def get_detail_default_fields(cls, model: type) -> list[str]: ...
    @classmethod
    def get_listing_default_fields(cls, model: type) -> list[str]: ...
    @classmethod
    def get_nested_default_fields(cls, model: type) -> list[str]: ...
    def check_query_parameters(self, queryset: QuerySet[Any]) -> None: ...
    def get_serializer_class(self) -> type[BaseSerializer]: ...
    def get_serializer_context(self) -> dict[str, Any]: ...
    def get_renderer_context(self) -> dict[str, Any]: ...
    @classmethod
    def get_urlpatterns(cls) -> list[Any]: ...
    @classmethod
    def get_model_listing_urlpath(cls, model: type, namespace: str = "") -> str | None: ...
    @classmethod
    def get_object_detail_urlpath(cls, model: type, pk: Any, namespace: str = "") -> str | None: ...

class PagesAPIViewSet(BaseAPIViewSet):
    base_serializer_class: type[PageSerializer]  # type: ignore[assignment]
    filter_backends: list[type[BaseFilterBackend]]
    known_query_parameters: frozenset[str]
    find_query_parameters: list[str]
    body_fields: list[str]
    meta_fields: list[str]
    listing_default_fields: list[str]
    nested_default_fields: list[str]
    detail_only_fields: list[str]
    name: str
    model: type[Page]  # type: ignore[assignment]
    @classmethod
    def get_detail_default_fields(cls, model: type) -> list[str]: ...
    @classmethod
    def get_listing_default_fields(cls, model: type) -> list[str]: ...
    def get_root_page(self) -> Page: ...
    def get_base_queryset(self) -> QuerySet[Page]: ...
    def get_queryset(self) -> QuerySet[Page]: ...
    def get_object(self) -> Page: ...
    def find_object(self, queryset: QuerySet[Any], request: Request) -> Page | None: ...
    def get_serializer_context(self) -> dict[str, Any]: ...
