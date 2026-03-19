from typing import Any, TypeVar

from django import forms
from django.core import validators
from django.db.models import Model, QuerySet
from django.forms.widgets import TextInput
from wagtail.models.media import Collection

_M = TypeVar("_M", bound=Model)

class URLOrAbsolutePathValidator(validators.URLValidator):
    @staticmethod
    def is_absolute_path(value: str) -> bool: ...
    def __call__(self, value: str) -> None: ...

class URLOrAbsolutePathField(forms.URLField):
    widget: type[TextInput]
    default_validators: list[URLOrAbsolutePathValidator]
    def to_python(self, value: str) -> str: ...

class ExternalLinkChooserForm(forms.Form):
    url: URLOrAbsolutePathField
    link_text: forms.CharField

class AnchorLinkChooserForm(forms.Form):
    url: forms.CharField
    link_text: forms.CharField

class EmailLinkChooserForm(forms.Form):
    email_address: forms.EmailField
    link_text: forms.CharField
    subject: forms.CharField
    body: forms.CharField

class PhoneLinkChooserForm(forms.Form):
    phone_number: forms.CharField
    link_text: forms.CharField

class BaseFilterForm(forms.Form):
    is_searching: bool
    is_filtering_by_collection: bool
    search_query: str | None
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def filter(self, objects: QuerySet[_M]) -> QuerySet[_M]: ...

class SearchFilterMixin(forms.Form):
    q: forms.CharField
    def filter(self, objects: QuerySet[_M]) -> QuerySet[_M]: ...

class CollectionFilterMixin(forms.Form):
    def __init__(self, *args: Any, collections: QuerySet[Collection] | None = None, **kwargs: Any) -> None: ...
    def filter(self, objects: QuerySet[_M]) -> QuerySet[_M]: ...

class LocaleFilterMixin(forms.Form):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def filter(self, objects: QuerySet[_M]) -> QuerySet[_M]: ...
