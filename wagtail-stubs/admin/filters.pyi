from collections.abc import Callable
from typing import Any

from django.db import models
from django.forms import Widget
from django.http import HttpRequest, QueryDict
from django.utils.functional import cached_property as cached_property
from django_filters.widgets import SuffixedMultiWidget
from wagtail.admin.models import popular_tags_for_model as popular_tags_for_model
from wagtail.admin.utils import get_user_display_name as get_user_display_name
from wagtail.admin.widgets import (
    AdminDateInput as AdminDateInput,
)
from wagtail.admin.widgets import (
    BooleanRadioSelect as BooleanRadioSelect,
)
from wagtail.admin.widgets import (
    FilteredSelect as FilteredSelect,
)
from wagtail.coreutils import (
    get_content_languages as get_content_languages,
)
from wagtail.coreutils import (
    get_content_type_label as get_content_type_label,
)
from wagtail.models import Locale as Locale
from wagtail.permission_policies.base import BasePermissionPolicy
import django_filters

class DateRangePickerWidget(SuffixedMultiWidget):
    template_name: str
    suffixes: list[str]
    def __init__(self, attrs: dict[str, str] | None = None) -> None: ...
    def decompress(self, value: slice | None) -> list[str | None]: ...

class FilteredModelChoiceIterator(django_filters.fields.ModelChoiceIterator):
    def choice(self, obj: models.Model) -> tuple[str, str, models.QuerySet[models.Model]]: ...

class FilteredModelChoiceField(django_filters.fields.ModelChoiceField):
    widget: type[FilteredSelect]
    iterator: type[FilteredModelChoiceIterator]
    filter_accessor: str | Callable[[models.Model], models.QuerySet[models.Model]]
    def __init__(
        self,
        queryset: models.QuerySet[models.Model] | models.manager.Manager[models.Model] | None = None,
        *,
        filter_accessor: str | Callable[[models.Model], models.QuerySet[models.Model]],
        filter_field: str,
        empty_label: str | None = ...,
        required: bool = ...,
        widget: Widget | type[Widget] | None = ...,
        label: str | None = ...,
        initial: str | None = ...,
        help_text: str = ...,
        to_field_name: str | None = ...,
        limit_choices_to: dict[str, str] | models.Q | None = ...,
        blank: bool = ...,
        **kwargs: str | bool | int | None,
    ) -> None: ...
    def get_filter_value(self, obj: models.Model) -> models.QuerySet[models.Model]: ...

class FilteredModelChoiceFilter(django_filters.ModelChoiceFilter):
    field_class: type[FilteredModelChoiceField]

class LocaleFilter(django_filters.ChoiceFilter):
    def filter(self, qs: models.QuerySet[models.Model], language_code: str) -> models.QuerySet[models.Model]: ...

class WagtailFilterSet(django_filters.FilterSet):
    def __init__(
        self,
        data: QueryDict | dict[str, str] | None = None,
        queryset: models.QuerySet[models.Model] | None = None,
        *,
        request: HttpRequest | None = None,
        prefix: str | None = None,
    ) -> None: ...
    @classmethod
    def filter_for_lookup(
        cls, field: models.Field, lookup_type: str
    ) -> tuple[type[django_filters.Filter], dict[str, Any]]: ...

class ContentTypeModelChoiceField(django_filters.fields.ModelChoiceField):
    def label_from_instance(self, obj: models.Model) -> str: ...

class ContentTypeFilter(django_filters.ModelChoiceFilter):
    field_class: type[ContentTypeModelChoiceField]

class ContentTypeModelMultipleChoiceField(django_filters.fields.ModelMultipleChoiceField):
    def label_from_instance(self, obj: models.Model) -> str: ...

class MultipleContentTypeFilter(django_filters.ModelMultipleChoiceFilter):
    field_class: type[ContentTypeModelMultipleChoiceField]

class UserModelMultipleChoiceField(django_filters.fields.ModelMultipleChoiceField):
    def label_from_instance(self, obj: models.Model) -> str: ...

class MultipleUserFilter(django_filters.ModelMultipleChoiceFilter):
    field_class: type[UserModelMultipleChoiceField]

class CollectionChoiceIterator(django_filters.fields.ModelChoiceIterator):
    @cached_property
    def min_depth(self) -> int: ...
    def choice(self, obj: models.Model) -> tuple[int, str]: ...

class CollectionChoiceField(django_filters.fields.ModelChoiceField):
    iterator: type[CollectionChoiceIterator]

class CollectionFilter(django_filters.ModelChoiceFilter):
    field_class: type[CollectionChoiceField]

class PopularTagsFilter(django_filters.MultipleChoiceFilter):
    use_subquery: bool
    def __init__(
        self,
        field_name: str | None = None,
        lookup_expr: str | None = None,
        *,
        use_subquery: bool = False,
        label: str | None = None,
        method: str | Callable[..., models.QuerySet[models.Model]] | None = None,
        distinct: bool = ...,
        exclude: bool = ...,
        conjoined: bool = ...,
        null_value: str = ...,
        **kwargs: str | bool | int | Widget | type[Widget] | None,
    ) -> None: ...
    def filter(self, qs: models.QuerySet[models.Model], value: list[str]) -> models.QuerySet[models.Model]: ...

class BaseMediaFilterSet(WagtailFilterSet):
    permission_policy: BasePermissionPolicy | None
    usage_count: bool
    def __init__(
        self,
        data: QueryDict | dict[str, str] | None = None,
        queryset: models.QuerySet[models.Model] | None = None,
        *,
        request: HttpRequest | None = None,
        prefix: str | None = None,
        is_searching: bool | None = None,
    ) -> None: ...
