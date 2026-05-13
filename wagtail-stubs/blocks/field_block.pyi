from collections.abc import Callable, Iterable, Iterator, Sequence
from decimal import Decimal
from typing import Any
import datetime

from django import forms
from django.db.models import Model
from django.forms.utils import _DataT, _FilesT
from django.utils.functional import _StrPromise, cached_property
from wagtail.rich_text import RichText
from wagtail.telepath import Adapter

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

type _Validator = Callable[[Any], None]

class FieldBlock(Block):
    @property
    def field(self) -> forms.Field: ...
    def id_for_label(self, prefix: str) -> str | None: ...
    def value_from_form(self, value: Any) -> Any: ...
    def value_for_form(self, value: Any) -> Any: ...
    def value_from_datadict(self, data: _DataT, files: _FilesT, prefix: str) -> Any: ...
    def value_omitted_from_data(self, data: _DataT, files: _FilesT, prefix: str) -> bool: ...
    def clean(self, value: Any) -> Any: ...
    @property
    def required(self) -> bool: ...
    def get_form_state(self, value: Any) -> Any: ...
    def get_description(self) -> str: ...

class FieldBlockAdapter(Adapter):
    js_constructor: str
    def js_args(self, block: FieldBlock) -> list[Any]: ...
    @cached_property
    def media(self) -> forms.Media: ...

class CharBlock(FieldBlock):
    search_index: bool
    field: forms.CharField
    def __init__(
        self,
        required: bool = True,
        help_text: str | _StrPromise | None = None,
        max_length: int | None = None,
        min_length: int | None = None,
        validators: Sequence[_Validator] = (),
        search_index: bool = True,
        **kwargs: Any,
    ) -> None: ...
    def get_searchable_content(self, value: str) -> list[str]: ...

class TextBlock(FieldBlock):
    field_options: dict[str, Any]
    rows: int
    search_index: bool
    def __init__(
        self,
        required: bool = True,
        help_text: str | _StrPromise | None = None,
        rows: int = 1,
        max_length: int | None = None,
        min_length: int | None = None,
        search_index: bool = True,
        validators: Sequence[_Validator] = (),
        **kwargs: Any,
    ) -> None: ...
    @cached_property
    def field(self) -> forms.CharField: ...  # type: ignore[override]
    def get_searchable_content(self, value: str) -> list[str]: ...

class BlockQuoteBlock(TextBlock):
    def render_basic(self, value: str, context: dict[str, Any] | None = None) -> str: ...

class FloatBlock(FieldBlock):
    field: forms.FloatField
    def __init__(
        self,
        required: bool = True,
        help_text: str | _StrPromise | None = None,
        max_value: float | None = None,
        min_value: float | None = None,
        validators: Sequence[_Validator] = (),
        **kwargs: Any,
    ) -> None: ...

class DecimalBlock(FieldBlock):
    field: forms.DecimalField
    def __init__(
        self,
        required: bool = True,
        help_text: str | _StrPromise | None = None,
        max_value: Decimal | float | None = None,
        min_value: Decimal | float | None = None,
        max_digits: int | None = None,
        decimal_places: int | None = None,
        validators: Sequence[_Validator] = (),
        **kwargs: Any,
    ) -> None: ...
    def to_python(self, value: str | float | Decimal | None) -> Decimal | None: ...

class RegexBlock(FieldBlock):
    field: forms.RegexField
    def __init__(
        self,
        regex: str,
        required: bool = True,
        help_text: str | _StrPromise | None = None,
        max_length: int | None = None,
        min_length: int | None = None,
        error_messages: dict[str, str] | None = None,
        validators: Sequence[_Validator] = (),
        *args: Any,
        **kwargs: Any,
    ) -> None: ...

class URLBlock(FieldBlock):
    field: forms.URLField
    def __init__(
        self,
        required: bool = True,
        help_text: str | _StrPromise | None = None,
        max_length: int | None = None,
        min_length: int | None = None,
        validators: Sequence[_Validator] = (),
        **kwargs: Any,
    ) -> None: ...

class BooleanBlock(FieldBlock):
    field: forms.BooleanField
    def __init__(
        self,
        required: bool = True,
        help_text: str | _StrPromise | None = None,
        **kwargs: Any,
    ) -> None: ...
    def get_form_state(self, value: Any) -> bool: ...

class DateBlock(FieldBlock):
    field_options: dict[str, Any]
    format: str | None
    def __init__(
        self,
        required: bool = True,
        help_text: str | _StrPromise | None = None,
        format: str | None = None,
        validators: Sequence[_Validator] = (),
        **kwargs: Any,
    ) -> None: ...
    @cached_property
    def field(self) -> forms.DateField: ...  # type: ignore[override]
    def to_python(self, value: str | datetime.date | None) -> datetime.date | None: ...

class TimeBlock(FieldBlock):
    field_options: dict[str, Any]
    format: str | None
    def __init__(
        self,
        required: bool = True,
        help_text: str | _StrPromise | None = None,
        format: str | None = None,
        validators: Sequence[_Validator] = (),
        **kwargs: Any,
    ) -> None: ...
    @cached_property
    def field(self) -> forms.TimeField: ...  # type: ignore[override]
    def to_python(self, value: str | datetime.time | None) -> datetime.time | None: ...

class DateTimeBlock(FieldBlock):
    field_options: dict[str, Any]
    format: str | None
    def __init__(
        self,
        required: bool = True,
        help_text: str | _StrPromise | None = None,
        format: str | None = None,
        validators: Sequence[_Validator] = (),
        **kwargs: Any,
    ) -> None: ...
    @cached_property
    def field(self) -> forms.DateTimeField: ...  # type: ignore[override]
    def to_python(self, value: str | datetime.datetime | None) -> datetime.datetime | None: ...

class EmailBlock(FieldBlock):
    field: forms.EmailField
    def __init__(
        self,
        required: bool = True,
        help_text: str | _StrPromise | None = None,
        validators: Sequence[_Validator] = (),
        **kwargs: Any,
    ) -> None: ...

class IntegerBlock(FieldBlock):
    field: forms.IntegerField
    def __init__(
        self,
        required: bool = True,
        help_text: str | _StrPromise | None = None,
        min_value: int | None = None,
        max_value: int | None = None,
        validators: Sequence[_Validator] = (),
        **kwargs: Any,
    ) -> None: ...

type _StrOrPromise = str | _StrPromise

type _ChoiceValue = str | int | float | _StrPromise
type _ChoiceLabel = _StrOrPromise

type _ChoiceType = (
    list[tuple[_ChoiceValue, _ChoiceLabel]]
    | list[tuple[_ChoiceLabel, list[tuple[_ChoiceValue, _ChoiceLabel]]]]
    | Iterable[tuple[_ChoiceValue, _ChoiceLabel | list[tuple[_ChoiceValue, _ChoiceLabel]]]]
    | Callable[[], Iterable[tuple[_ChoiceValue, _ChoiceLabel | list[tuple[_ChoiceValue, _ChoiceLabel]]]]]
)

class BaseChoiceBlock(FieldBlock):
    choices: _ChoiceType
    search_index: bool
    def __init__(
        self,
        choices: _ChoiceType | None = None,
        default: Any = None,
        required: bool = True,
        help_text: str | _StrPromise | None = None,
        search_index: bool = True,
        widget: type[forms.Widget] | forms.Widget | None = None,
        validators: Sequence[_Validator] = (),
        **kwargs: Any,
    ) -> None: ...
    def normalize_choice(self, value: Any) -> Any: ...

class ChoiceBlock(BaseChoiceBlock):
    field: forms.ChoiceField  # type: ignore[assignment]
    def get_field(self, **kwargs: Any) -> forms.ChoiceField: ...
    def deconstruct(self) -> tuple[str, list[Any], dict[str, Any]]: ...
    def get_searchable_content(self, value: str) -> list[str]: ...

class MultipleChoiceBlock(BaseChoiceBlock):
    def get_field(self, **kwargs: Any) -> forms.MultipleChoiceField: ...
    def deconstruct(self) -> tuple[str, list[Any], dict[str, Any]]: ...
    def get_searchable_content(self, value: str | list[str]) -> list[str]: ...

class RichTextBlock(FieldBlock):
    field_options: dict[str, Any]
    max_length: int | None
    editor: str
    features: list[str] | None
    search_index: bool
    def __init__(
        self,
        required: bool = True,
        help_text: str | _StrPromise | None = None,
        editor: str = "default",
        features: list[str] | None = None,
        max_length: int | None = None,
        min_length: int | None = None,
        validators: Sequence[_Validator] = (),
        search_index: bool = True,
        **kwargs: Any,
    ) -> None: ...
    def to_python(self, value: str | RichText) -> RichText: ...
    def get_prep_value(self, value: RichText) -> str: ...
    def normalize(self, value: str | RichText) -> RichText: ...
    @cached_property
    def field(self) -> forms.CharField: ...  # type: ignore[override]
    def value_for_form(self, value: RichText) -> str: ...
    def value_from_form(self, value: str) -> RichText: ...
    def get_searchable_content(self, value: RichText) -> list[str]: ...
    def extract_references(self, value: RichText) -> Iterator[tuple[type[Model], str, str, str]]: ...

class RawHTMLBlock(FieldBlock):
    field: forms.CharField
    def __init__(
        self,
        required: bool = True,
        help_text: str | _StrPromise | None = None,
        max_length: int | None = None,
        min_length: int | None = None,
        validators: Sequence[_Validator] = (),
        **kwargs: Any,
    ) -> None: ...
    def get_default(self) -> str: ...
    def to_python(self, value: str) -> str: ...
    def normalize(self, value: str) -> str: ...
    def get_prep_value(self, value: str) -> str: ...
    def value_for_form(self, value: str) -> str: ...
    def value_from_form(self, value: str) -> str: ...

class ChooserBlock(FieldBlock):
    _required: bool
    _help_text: str | _StrPromise | None
    _validators: Sequence[_Validator]
    def __init__(
        self,
        required: bool = True,
        help_text: str | _StrPromise | None = None,
        validators: Sequence[_Validator] = (),
        **kwargs: Any,
    ) -> None: ...
    target_model: type[Model] | str
    @cached_property
    def model_class(self) -> type[Model]: ...
    @cached_property
    def widget(self) -> forms.Widget: ...
    @cached_property
    def field(self) -> forms.ModelChoiceField: ...  # type: ignore[override]
    def to_python(self, value: int | str | None) -> Model | None: ...
    def bulk_to_python(self, values: list[int | str | None]) -> list[Model | None]: ...
    def get_prep_value(self, value: Model | None) -> int | str | None: ...
    def value_from_form(self, value: int | str | Model | None) -> Model | None: ...
    def get_form_state(self, value: Model | None) -> dict[str, Any] | None: ...
    def clean(self, value: Model | int | str | None) -> Model | None: ...
    def extract_references(self, value: Model | None) -> Iterator[tuple[type[Model], str, str, str]]: ...

class PageChooserBlock(ChooserBlock):
    page_type: list[str | type[Model]]
    can_choose_root: bool
    def __init__(
        self,
        page_type: list[str | type[Model]] | str | type[Model] | None = None,
        can_choose_root: bool = False,
        target_model: list[str | type[Model]] | str | type[Model] | None = None,
        **kwargs: Any,
    ) -> None: ...
    @cached_property
    def target_model(self) -> type[Model]: ...  # type: ignore[override]
    @cached_property
    def target_models(self) -> list[type[Model]]: ...
    @cached_property
    def widget(self) -> forms.Widget: ...
    def get_form_state(self, value: Model | None) -> dict[str, str | int] | None: ...
    def render_basic(self, value: Model | None, context: dict[str, Any] | None = None) -> str: ...
    def deconstruct(self) -> tuple[str, list[Any], dict[str, Any]]: ...

DECONSTRUCT_ALIASES: dict[type[Block], str]
