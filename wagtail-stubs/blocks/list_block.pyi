from collections.abc import Iterator, Mapping, MutableSequence
from typing import Any, overload

from django import forms
from django.core import checks
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList, _DataT, _FilesT
from django.utils.functional import cached_property
from telepath import Adapter

from .base import Block, BoundBlock
from .definition_lookup import BlockDefinitionLookup, BlockDefinitionLookupBuilder

__all__ = ["ListBlock", "ListBlockValidationError"]

class ListBlockValidationError(ValidationError):
    non_block_errors: ErrorList
    block_errors: dict[int, ValidationError]
    def __init__(
        self,
        block_errors: Mapping[int, ValidationError | ErrorList | list[ValidationError]]
        | list[ValidationError | None]
        | None = None,
        non_block_errors: ErrorList | list[str | ValidationError] | None = None,
    ) -> None: ...
    def as_json_data(self) -> dict[str, Any]: ...

class ListValue(MutableSequence[Any]):
    class ListChild(BoundBlock):
        original_id: str | None
        id: str
        def __init__(self, *args: Any, **kwargs: Any) -> None: ...
        def get_prep_value(self) -> dict[str, Any]: ...

    list_block: ListBlock[Any]
    bound_blocks: list[ListChild]
    def __init__(
        self,
        list_block: ListBlock[Any],
        values: list[Any] | None = None,
        bound_blocks: list[ListChild] | None = None,
    ) -> None: ...
    @overload
    def __getitem__(self, i: int) -> Any: ...
    @overload
    def __getitem__(self, i: slice) -> list[Any]: ...
    def __getitem__(self, i: int | slice) -> Any: ...  # type: ignore[override]
    def __setitem__(self, i: int, item: Any) -> None: ...  # type: ignore[override]
    def __delitem__(self, i: int) -> None: ...  # type: ignore[override]
    def __len__(self) -> int: ...
    def insert(self, i: int, item: Any) -> None: ...

class ListBlock[BlockT: Block](Block):
    child_block: BlockT
    search_index: bool
    @overload
    def __init__(
        self,
        child_block: BlockT | type[BlockT],
        /,
        search_index: bool = True,
        **kwargs: Any,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        child_block: BlockT | type[BlockT],
        search_index: bool = True,
        **kwargs: Any,
    ) -> None: ...
    @classmethod
    def construct_from_lookup(  # type: ignore[override]
        cls, lookup: BlockDefinitionLookup, *args: Any, **kwargs: Any
    ) -> ListBlock[Any]: ...
    def value_from_datadict(self, data: _DataT, files: _FilesT, prefix: str) -> ListValue: ...
    def value_omitted_from_data(self, data: _DataT, files: _FilesT, prefix: str) -> bool: ...
    def clean(self, value: ListValue | list[Any]) -> ListValue: ...
    def normalize(self, value: ListValue | list[Any]) -> ListValue: ...
    def empty_value(self) -> ListValue: ...
    def to_python(self, value: list[Any]) -> ListValue: ...
    def bulk_to_python(self, values: list[list[Any]]) -> list[ListValue]: ...
    def get_prep_value(self, value: ListValue | list[Any]) -> list[dict[str, Any]]: ...
    def get_form_state(self, value: ListValue | list[Any]) -> list[dict[str, Any]]: ...
    def get_api_representation(self, value: ListValue, context: dict[str, Any] | None = None) -> list[Any]: ...
    def render_basic(self, value: ListValue, context: dict[str, Any] | None = None) -> str: ...
    def get_searchable_content(self, value: ListValue) -> list[str]: ...
    def extract_references(self, value: ListValue) -> Iterator[tuple[type, str, str, str]]: ...
    def get_block_by_content_path(self, value: ListValue, path_elements: list[str]) -> BoundBlock | None: ...
    def check(self, **kwargs: Any) -> list[checks.Error]: ...
    def deconstruct_with_lookup(
        self, lookup: BlockDefinitionLookupBuilder
    ) -> tuple[str, tuple[Any, ...], dict[str, Any]]: ...
    MUTABLE_META_ATTRIBUTES: list[str]

    class Meta:
        icon: str
        form_classname: None
        min_num: int | None
        max_num: int | None
        collapsed: bool

class ListBlockAdapter(Adapter):
    js_constructor: str
    def js_args(self, block: ListBlock[Any]) -> list[Any]: ...
    @cached_property
    def media(self) -> forms.Media: ...  # type: ignore[override]
