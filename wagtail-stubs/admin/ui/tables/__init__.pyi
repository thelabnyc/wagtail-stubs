from collections import OrderedDict
from collections.abc import Callable, Generator, Iterator, Mapping, Sequence
from typing import Any

from django.forms import Media, MediaDefiningClass
from django.template.backends.base import _EngineTemplate
from django.utils.functional import cached_property as cached_property
from wagtail.admin.ui.components import Component as Component
from wagtail.admin.widgets.button import Button
from wagtail.coreutils import get_locales_display_names as get_locales_display_names
from wagtail.coreutils import multigetattr as multigetattr
from wagtail.models.i18n import Locale as Locale

class BaseColumn(metaclass=MediaDefiningClass):
    class Header:
        column: BaseColumn
        def __init__(self, column: BaseColumn) -> None: ...
        def render_html(self, parent_context: dict[str, Any]) -> str: ...

    class Cell:
        column: BaseColumn
        instance: Any
        def __init__(self, column: BaseColumn, instance: Any) -> None: ...
        def render_html(self, parent_context: dict[str, Any]) -> str: ...

    header_template_name: str
    cell_template_name: str | None
    name: str
    accessor: str | Callable[..., Any]
    label: str
    classname: str | None
    sort_key: str | None
    header: BaseColumn.Header
    width: str | None
    ascending_title_text: str | None
    descending_title_text: str | None
    def __init__(
        self,
        name: str,
        label: str | None = None,
        accessor: str | Callable[..., Any] | None = None,
        classname: str | None = None,
        sort_key: str | None = None,
        width: str | None = None,
        ascending_title_text: str | None = None,
        descending_title_text: str | None = None,
    ) -> None: ...
    def get_header_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...
    @cached_property
    def header_template(self) -> _EngineTemplate: ...
    @cached_property
    def cell_template(self) -> _EngineTemplate: ...
    def render_header_html(self, parent_context: dict[str, Any]) -> str: ...
    def get_cell_context_data(self, instance: Any, parent_context: dict[str, Any]) -> dict[str, Any]: ...
    def render_cell_html(self, instance: Any, parent_context: dict[str, Any]) -> str: ...
    def get_cell(self, instance: Any) -> BaseColumn.Cell: ...

class Column(BaseColumn):
    cell_template_name: str
    empty_value_display: str
    def get_value(self, instance: Any) -> Any: ...
    def get_cell_context_data(self, instance: Any, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class NumberColumn(Column):
    def get_cell_context_data(self, instance: Any, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class ButtonsColumnMixin:
    buttons: list[Button]
    def get_cell_context_data(self, instance: Any, parent_context: dict[str, Any]) -> dict[str, Any]: ...
    def get_buttons(self, instance: Any, parent_context: dict[str, Any]) -> list[Button]: ...

class TitleColumn(Column):
    cell_template_name: str
    empty_value_display: str
    url_name: str | None
    label_prefix: str | None
    link_attrs: dict[str, str]
    link_classname: str | None
    id_accessor: str
    def __init__(
        self,
        name: str,
        url_name: str | None = None,
        get_url: Callable[[Any], str | None] | None = None,
        get_title_id: Callable[[Any], str | None] | None = None,
        label_prefix: str | None = None,
        get_label_id: Callable[[Any], str | None] | None = None,
        link_classname: str | None = None,
        link_attrs: dict[str, str] | None = None,
        id_accessor: str = "pk",
        **kwargs: Any,
    ) -> None: ...
    def get_cell_context_data(self, instance: Any, parent_context: dict[str, Any]) -> dict[str, Any]: ...
    def get_link_attrs(self, instance: Any, parent_context: dict[str, Any]) -> dict[str, str]: ...
    def get_link_url(self, instance: Any, parent_context: dict[str, Any]) -> str | None: ...
    def get_title_id(self, instance: Any, parent_context: dict[str, Any]) -> str | None: ...
    def get_label_id(self, instance: Any, parent_context: dict[str, Any]) -> str | None: ...

class StatusFlagColumn(Column):
    cell_template_name: str
    true_label: str | None
    false_label: str | None
    def __init__(
        self, name: str, true_label: str | None = None, false_label: str | None = None, **kwargs: Any
    ) -> None: ...

class StatusTagColumn(Column):
    cell_template_name: str
    primary: Callable[[Any], bool] | bool | None
    def __init__(self, name: str, primary: Callable[[Any], bool] | bool | None = None, **kwargs: Any) -> None: ...
    def get_primary(self, instance: Any) -> bool | None: ...
    def get_cell_context_data(self, instance: Any, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class BooleanColumn(Column):
    cell_template_name: str
    def get_value(self, instance: Any) -> bool | None: ...

class LiveStatusTagColumn(StatusTagColumn):
    def __init__(self, **kwargs: Any) -> None: ...

class LocaleColumn(Column):
    cell_template_name: str
    def __init__(self, **kwargs: Any) -> None: ...
    def get_cell_context_data(self, instance: Any, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class DateColumn(Column):
    cell_template_name: str

class UpdatedAtColumn(DateColumn):
    def __init__(self, **kwargs: Any) -> None: ...

class UserColumn(Column):
    cell_template_name: str
    blank_display_name: str
    def __init__(self, name: str, blank_display_name: str = "", **kwargs: Any) -> None: ...
    def get_cell_context_data(self, instance: Any, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class BulkActionsCheckboxColumn(BaseColumn):
    header_template_name: str
    cell_template_name: str
    obj_type: str
    def __init__(self, *args: Any, obj_type: str, **kwargs: Any) -> None: ...
    def get_aria_describedby(self, instance: Any) -> str: ...
    def get_cell_context_data(self, instance: Any, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class UsageCountColumn(Column):
    cell_template_name: str

class ReferencesColumn(Column):
    cell_template_name: str
    describe_on_delete: bool
    def __init__(
        self,
        name: str,
        label: str | None = None,
        accessor: str | Callable[..., Any] | None = None,
        classname: str | None = None,
        sort_key: str | None = None,
        width: str | None = None,
        get_url: Callable[[Any], str | None] | None = None,
        describe_on_delete: bool = False,
    ) -> None: ...
    def get_edit_url(self, instance: Any) -> str | None: ...
    def get_cell_context_data(self, instance: Any, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class DownloadColumn(Column):
    cell_template_name: str
    def get_cell_context_data(self, instance: Any, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class RelatedObjectsColumn(Column):
    cell_template_name: str
    def get_value(self, instance: Any) -> Any: ...

class Table(Component):
    template_name: str
    classname: str
    header_row_classname: str
    ascending_title_text_format: str
    descending_title_text_format: str
    columns: OrderedDict[str, BaseColumn]
    caption: str | None
    data: Sequence[Any]
    base_url: str | None
    ordering: str | None
    base_attrs: dict[str, str]
    def __init__(
        self,
        columns: Sequence[BaseColumn],
        data: Sequence[Any],
        template_name: str | None = None,
        base_url: str | None = None,
        ordering: str | None = None,
        classname: str | None = None,
        attrs: dict[str, str] | None = None,
        caption: str | None = None,
    ) -> None: ...
    def get_caption(self) -> str | None: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...
    @property
    def media(self) -> Media: ...
    @property
    def rows(self) -> Generator[Table.Row]: ...
    @property
    def row_count(self) -> int: ...
    @property
    def attrs(self) -> dict[str, str]: ...
    def get_row_classname(self, instance: Any) -> str: ...
    def get_row_attrs(self, instance: Any) -> dict[str, str]: ...
    def has_column_widths(self) -> bool: ...
    def get_ascending_title_text(self, column: BaseColumn) -> str | None: ...
    def get_descending_title_text(self, column: BaseColumn) -> str | None: ...
    class Row(Mapping[str, BaseColumn.Cell]):
        table: Table
        columns: OrderedDict[str, BaseColumn]
        instance: Any
        index: int
        def __init__(self, table: Table, instance: Any, index: int) -> None: ...
        def __len__(self) -> int: ...
        def __getitem__(self, key: str) -> BaseColumn.Cell: ...
        def __iter__(self) -> Iterator[str]: ...
        @cached_property
        def classname(self) -> str: ...
        @cached_property
        def attrs(self) -> dict[str, str]: ...
