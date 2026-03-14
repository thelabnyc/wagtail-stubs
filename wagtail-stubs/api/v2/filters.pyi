from .utils import BadRequestError as BadRequestError, parse_boolean as parse_boolean
from rest_framework.filters import BaseFilterBackend
from wagtail.models import Locale as Locale, Page as Page
from wagtail.search.backends import get_search_backend as get_search_backend
from wagtail.search.backends.base import FilterFieldError as FilterFieldError, OrderByFieldError as OrderByFieldError

class FieldsFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view): ...

class OrderingFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view): ...

class SearchFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view): ...

class ChildOfFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view): ...

class AncestorOfFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view): ...

class DescendantOfFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view): ...

class TranslationOfFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view): ...

class LocaleFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view): ...
