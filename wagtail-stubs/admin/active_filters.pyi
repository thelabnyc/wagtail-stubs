import django_filters
from _typeshed import Incomplete
from collections.abc import Generator
from django.forms import BoundField
from django.http import QueryDict
from typing import NamedTuple
from wagtail.utils.registry import ObjectTypeRegistry as ObjectTypeRegistry
from wagtail.utils.utils import flatten_choices as flatten_choices

class ActiveFilter(NamedTuple):
    auto_id: Incomplete
    field_label: Incomplete
    value: Incomplete
    removed_filter_url: Incomplete

class BaseFilterAdapter:
    filter: Incomplete
    bound_field: Incomplete
    name: Incomplete
    value: Incomplete
    base_url: Incomplete
    query_dict: Incomplete
    def __init__(self, filter: django_filters.Filter, bound_field: BoundField, value, base_url: str, query_dict: QueryDict) -> None: ...
    def get_url_without_filter_param(self, param): ...
    def get_url_without_filter_param_value(self, param, value): ...
    def get_active_filters(self) -> Generator[Incomplete]: ...

class ChoiceFilterAdapter(BaseFilterAdapter):
    def get_active_filters(self) -> Generator[Incomplete]: ...

class MultipleChoiceFilterAdapter(BaseFilterAdapter):
    def get_active_filters(self) -> Generator[Incomplete, Incomplete]: ...

class ModelChoiceFilterAdapter(BaseFilterAdapter):
    def get_active_filters(self) -> Generator[Incomplete]: ...

class ModelMultipleChoiceFilterAdapter(BaseFilterAdapter):
    def get_active_filters(self) -> Generator[Incomplete, Incomplete]: ...

class RangeFilterAdapter(BaseFilterAdapter):
    empty_value_label: Incomplete
    def format_value(self, value): ...
    def get_active_filters(self) -> Generator[Incomplete]: ...

class DateFromToRangeFilterAdapter(RangeFilterAdapter):
    def format_value(self, value): ...

filter_adapter_class_registry: Incomplete

def register_filter_adapter_class(filter_class: type[django_filters.Filter], adapter_class: type[BaseFilterAdapter] = None, exact_class: bool = False): ...
