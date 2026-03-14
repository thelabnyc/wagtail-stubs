from typing import Any

from django.db.models import QuerySet
from rest_framework.filters import BaseFilterBackend
from rest_framework.request import Request

from .utils import BadRequestError as BadRequestError, parse_boolean as parse_boolean
from wagtail.models import Locale as Locale, Page as Page
from wagtail.search.backends import get_search_backend as get_search_backend
from wagtail.search.backends.base import FilterFieldError as FilterFieldError, OrderByFieldError as OrderByFieldError

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
