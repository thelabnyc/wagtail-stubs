from collections.abc import Generator
from datetime import date
from typing import NamedTuple

from django.db import models
from django.db.models import QuerySet
from django.forms import BoundField
from django.http import QueryDict
from wagtail.utils.registry import ObjectTypeRegistry as ObjectTypeRegistry
from wagtail.utils.utils import flatten_choices as flatten_choices
import django_filters

type _FilterValue = str | list[str] | models.Model | QuerySet[models.Model] | slice

class ActiveFilter(NamedTuple):
    auto_id: str
    field_label: str
    value: str
    removed_filter_url: str

class BaseFilterAdapter:
    filter: django_filters.Filter
    bound_field: BoundField
    name: str
    value: _FilterValue
    base_url: str
    query_dict: QueryDict
    def __init__(
        self,
        filter: django_filters.Filter,
        bound_field: BoundField,
        value: _FilterValue,
        base_url: str,
        query_dict: QueryDict,
    ) -> None: ...
    def get_url_without_filter_param(self, param: str | list[str] | tuple[str, ...]) -> str: ...
    def get_url_without_filter_param_value(self, param: str, value: str | int) -> str: ...
    def get_active_filters(self) -> Generator[ActiveFilter]: ...

class ChoiceFilterAdapter(BaseFilterAdapter):
    def get_active_filters(self) -> Generator[ActiveFilter]: ...

class MultipleChoiceFilterAdapter(BaseFilterAdapter):
    def get_active_filters(self) -> Generator[ActiveFilter]: ...

class ModelChoiceFilterAdapter(BaseFilterAdapter):
    def get_active_filters(self) -> Generator[ActiveFilter]: ...

class ModelMultipleChoiceFilterAdapter(BaseFilterAdapter):
    def get_active_filters(self) -> Generator[ActiveFilter]: ...

class RangeFilterAdapter(BaseFilterAdapter):
    empty_value_label: str
    def format_value(self, value: str | float | date | None) -> str: ...
    def get_active_filters(self) -> Generator[ActiveFilter]: ...

class DateFromToRangeFilterAdapter(RangeFilterAdapter):
    def format_value(self, value: str | float | date | None) -> str: ...

filter_adapter_class_registry: ObjectTypeRegistry

def register_filter_adapter_class(
    filter_class: type[django_filters.Filter],
    adapter_class: type[BaseFilterAdapter] | None = ...,
    exact_class: bool = False,
) -> None: ...
