from typing import Any

from django import forms
from django.core.exceptions import ValidationError
from django.utils.functional import cached_property
from wagtail.admin.telepath import Adapter

class WidgetAdapter(Adapter):
    js_constructor: str
    def js_args(self, widget: forms.Widget) -> list[Any]: ...
    def get_media(self, widget: forms.Widget) -> forms.Media: ...
    @cached_property
    def media(self) -> forms.Media: ...

class CheckboxInputAdapter(WidgetAdapter):
    js_constructor: str

class RadioSelectAdapter(WidgetAdapter):
    js_constructor: str

class SelectAdapter(WidgetAdapter):
    js_constructor: str

class ValidationErrorAdapter(Adapter):
    js_constructor: str
    def js_args(self, error: ValidationError) -> list[list[str]]: ...
    @cached_property
    def media(self) -> forms.Media: ...
