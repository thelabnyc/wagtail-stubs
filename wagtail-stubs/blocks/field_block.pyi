import datetime
from decimal import Decimal
from typing import Any

from django import forms
from django.utils.functional import cached_property

from .base import Block

__all__ = [
    "FieldBlock",
    "CharBlock",
    "URLBlock",
    "RichTextBlock",
    "RawHTMLBlock",
    "ChooserBlock",
    "PageChooserBlock",
    "TextBlock",
    "BooleanBlock",
    "DateBlock",
    "TimeBlock",
    "DateTimeBlock",
    "ChoiceBlock",
    "MultipleChoiceBlock",
    "EmailBlock",
    "IntegerBlock",
    "FloatBlock",
    "DecimalBlock",
    "RegexBlock",
    "BlockQuoteBlock",
]

class FieldBlock(Block):
    @cached_property
    def field(self) -> forms.Field: ...
    def id_for_label(self, prefix: str) -> str | None: ...
    def value_from_form(self, value: Any) -> Any: ...
    def value_for_form(self, value: Any) -> Any: ...
    def value_from_datadict(self, data: dict[str, Any], files: dict[str, Any], prefix: str) -> Any: ...
    def value_omitted_from_data(self, data: dict[str, Any], files: dict[str, Any], prefix: str) -> bool: ...
    def clean(self, value: Any) -> Any: ...
    @property
    def required(self) -> bool: ...
    def get_form_state(self, value: Any) -> Any: ...
    def get_description(self) -> str: ...

class CharBlock(FieldBlock):
    def __init__(
        self,
        required: bool = True,
        help_text: str = "",
        max_length: int | None = None,
        min_length: int | None = None,
        search_index: bool = True,
        validators: list[Any] = ...,
        form_classname: str = "",
        **kwargs: Any,
    ) -> None: ...

class TextBlock(FieldBlock):
    rows: int
    def __init__(self, required: bool = True, help_text: str = "", rows: int = 1, max_length: int | None = None, min_length: int | None = None, search_index: bool = True, validators: list[Any] = ..., form_classname: str = "", **kwargs: Any) -> None: ...

class BlockQuoteBlock(TextBlock):
    def __init__(self, **kwargs: Any) -> None: ...

class FloatBlock(FieldBlock):
    def __init__(self, required: bool = True, max_value: float | None = None, min_value: float | None = None, **kwargs: Any) -> None: ...

class DecimalBlock(FieldBlock):
    def __init__(self, required: bool = True, max_value: Decimal | None = None, min_value: Decimal | None = None, max_digits: int | None = None, decimal_places: int | None = None, **kwargs: Any) -> None: ...

class RegexBlock(FieldBlock):
    def __init__(self, regex: str = "", help_text: str = "", required: bool = True, error_messages: dict[str, str] | None = None, **kwargs: Any) -> None: ...

class URLBlock(FieldBlock):
    def __init__(self, required: bool = True, help_text: str = "", max_length: int | None = None, min_length: int | None = None, validators: list[Any] = ..., **kwargs: Any) -> None: ...

class BooleanBlock(FieldBlock):
    def __init__(self, required: bool = True, help_text: str = "", **kwargs: Any) -> None: ...

class DateBlock(FieldBlock):
    def __init__(self, required: bool = True, help_text: str = "", format: str | None = None, **kwargs: Any) -> None: ...

class TimeBlock(FieldBlock):
    def __init__(self, required: bool = True, help_text: str = "", **kwargs: Any) -> None: ...

class DateTimeBlock(FieldBlock):
    def __init__(self, required: bool = True, help_text: str = "", format: str | None = None, **kwargs: Any) -> None: ...

class EmailBlock(FieldBlock):
    def __init__(self, required: bool = True, help_text: str = "", **kwargs: Any) -> None: ...

class IntegerBlock(FieldBlock):
    def __init__(self, required: bool = True, help_text: str = "", max_value: int | None = None, min_value: int | None = None, **kwargs: Any) -> None: ...

class ChoiceBlock(FieldBlock):
    choices: list[tuple[str, str]] | list[tuple[str, list[tuple[str, str]]]]
    def __init__(self, choices: list[Any] | None = None, required: bool = True, help_text: str = "", widget: type[forms.Widget] | forms.Widget | None = None, **kwargs: Any) -> None: ...

class MultipleChoiceBlock(FieldBlock):
    choices: list[tuple[str, str]] | list[tuple[str, list[tuple[str, str]]]]
    def __init__(self, choices: list[Any] | None = None, required: bool = True, help_text: str = "", widget: type[forms.Widget] | forms.Widget | None = None, **kwargs: Any) -> None: ...

class RichTextBlock(FieldBlock):
    def __init__(self, required: bool = True, help_text: str = "", editor: str = "default", features: list[str] | None = None, max_length: int | None = None, min_length: int | None = None, search_index: bool = True, **kwargs: Any) -> None: ...
    def get_searchable_content(self, value: Any) -> list[str]: ...

class RawHTMLBlock(FieldBlock):
    def __init__(self, required: bool = True, help_text: str = "", max_length: int | None = None, min_length: int | None = None, **kwargs: Any) -> None: ...

class ChooserBlock(FieldBlock):
    def __init__(self, required: bool = True, help_text: str = "", **kwargs: Any) -> None: ...
    @cached_property
    def target_model(self) -> type: ...
    @cached_property
    def widget(self) -> forms.Widget: ...

class PageChooserBlock(ChooserBlock):
    def __init__(self, page_type: list[str | type] | str | type | None = None, can_choose_root: bool = False, target_model: list[str | type] | str | type | None = None, **kwargs: Any) -> None: ...
