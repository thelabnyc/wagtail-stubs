from typing import Any

from django.forms import Media, widgets
from django.utils.functional import cached_property
from wagtail.admin.rich_text.converters.contentstate import ContentstateConverter
from wagtail.widget_adapters import WidgetAdapter

class DraftailRichTextArea(widgets.HiddenInput):
    template_name: str
    is_hidden: bool
    accepts_features: bool
    show_add_comment_button: bool
    options: dict[str, Any]
    plugins: list[Any]
    features: list[str]
    converter: ContentstateConverter

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def format_value(self, value: str | None) -> str: ...
    def get_context(self, name: str, value: Any, attrs: dict[str, Any] | None) -> dict[str, Any]: ...
    def value_from_datadict(self, data: dict[str, Any], files: dict[str, Any], name: str) -> str | None: ...
    @cached_property
    def media(self) -> Media: ...  # type: ignore[override]

class DraftailRichTextAreaAdapter(WidgetAdapter):
    js_constructor: str
    def js_args(self, widget: DraftailRichTextArea) -> list[Any]: ...
