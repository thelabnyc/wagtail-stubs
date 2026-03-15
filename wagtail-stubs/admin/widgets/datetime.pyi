from typing import Any

from django import forms
from django.forms import widgets

from wagtail.widget_adapters import WidgetAdapter

DEFAULT_DATE_FORMAT: str
DEFAULT_DATETIME_FORMAT: str
DEFAULT_TIME_FORMAT: str

class AdminDateInput(widgets.DateInput):
    template_name: str
    js_format: str
    def __init__(self, attrs: dict[str, Any] | None = None, format: str | None = None) -> None: ...
    def get_config(self) -> dict[str, str | int]: ...
    def get_context(self, name: str, value: Any, attrs: dict[str, Any] | None) -> dict[str, Any]: ...
    @property
    def media(self) -> forms.Media: ...

class AdminDateInputAdapter(WidgetAdapter):
    js_constructor: str
    def js_args(self, widget: AdminDateInput) -> list[dict[str, str | int]]: ...

class AdminTimeInput(widgets.TimeInput):
    template_name: str
    js_format: str
    def __init__(self, attrs: dict[str, Any] | None = None, format: str | None = None) -> None: ...
    def get_config(self) -> dict[str, str]: ...
    def get_context(self, name: str, value: Any, attrs: dict[str, Any] | None) -> dict[str, Any]: ...
    @property
    def media(self) -> forms.Media: ...

class AdminTimeInputAdapter(WidgetAdapter):
    js_constructor: str
    def js_args(self, widget: AdminTimeInput) -> list[dict[str, str]]: ...

class AdminDateTimeInput(widgets.DateTimeInput):
    template_name: str
    js_format: str
    js_time_format: str
    js_overlay_parent_selector: str
    def __init__(
        self,
        attrs: dict[str, Any] | None = None,
        format: str | None = None,
        time_format: str | None = None,
        js_overlay_parent_selector: str = "body",
    ) -> None: ...
    def get_config(self) -> dict[str, str | int]: ...
    def get_context(self, name: str, value: Any, attrs: dict[str, Any] | None) -> dict[str, Any]: ...
    @property
    def media(self) -> forms.Media: ...

class AdminDateTimeInputAdapter(WidgetAdapter):
    js_constructor: str
    def js_args(self, widget: AdminDateTimeInput) -> list[dict[str, str | int]]: ...
