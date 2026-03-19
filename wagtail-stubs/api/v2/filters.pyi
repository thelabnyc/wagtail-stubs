from typing import Any

from django.db.models import QuerySet
from rest_framework.filters import BaseFilterBackend
from rest_framework.request import Request
from wagtail.models.i18n import Locale as Locale
from wagtail.models.pages import Page as Page
from wagtail.search.backends import get_search_backend as get_search_backend
from wagtail.search.backends.base import FilterFieldError as FilterFieldError
from wagtail.search.backends.base import OrderByFieldError as OrderByFieldError

from .utils import BadRequestError as BadRequestError
from .utils import parse_boolean as parse_boolean

class FieldsFilter(BaseFilterBackend):
    def filter_queryset(self, request: Request, queryset: QuerySet[Any], view: Any) -> QuerySet[Any]: ...

class OrderingFilter(BaseFilterBackend):
    def filter_queryset(self, request: Request, queryset: QuerySet[Any], view: Any) -> QuerySet[Any]: ...

class SearchFilter(BaseFilterBackend):
    def filter_queryset(self, request: Request, queryset: QuerySet[Any], view: Any) -> QuerySet[Any]: ...

class ChildOfFilter(BaseFilterBackend):
    def filter_queryset(self, request: Request, queryset: QuerySet[Any], view: Any) -> QuerySet[Any]: ...

class AncestorOfFilter(BaseFilterBackend):
    def filter_queryset(self, request: Request, queryset: QuerySet[Any], view: Any) -> QuerySet[Any]: ...

class DescendantOfFilter(BaseFilterBackend):
    def filter_queryset(self, request: Request, queryset: QuerySet[Any], view: Any) -> QuerySet[Any]: ...

class TranslationOfFilter(BaseFilterBackend):
    def filter_queryset(self, request: Request, queryset: QuerySet[Any], view: Any) -> QuerySet[Any]: ...

class LocaleFilter(BaseFilterBackend):
    def filter_queryset(self, request: Request, queryset: QuerySet[Any], view: Any) -> QuerySet[Any]: ...
