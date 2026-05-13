from typing import Any

from django.utils.safestring import SafeString
from wagtail.admin.ui.tables import BaseColumn, BulkActionsCheckboxColumn, Column, Table
from wagtail.admin.ui.tables.orderable import OrderableTableMixin
from wagtail.models import Page

class PageTitleColumn(BaseColumn):
    header_template_name: str
    cell_template_name: str
    classname: str
    def get_header_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...
    def get_cell_context_data(self, instance: Page, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class ParentPageColumn(Column):
    cell_template_name: str
    def get_value(self, instance: Page) -> Page | None: ...

class PageStatusColumn(BaseColumn):
    cell_template_name: str

class BulkActionsColumn(BulkActionsCheckboxColumn):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_header_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class PageTypeColumn(Column):
    def get_header_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class NavigateToChildrenColumn(BaseColumn):
    cell_template_name: str
    def get_cell_context_data(self, instance: Page, parent_context: dict[str, Any]) -> dict[str, Any]: ...
    def render_header_html(self, parent_context: dict[str, Any]) -> SafeString: ...

class PageTable(OrderableTableMixin, Table):
    parent_page: Page | None
    show_locale_labels: bool
    actions_next_url: str | None
    def __init__(
        self,
        *args: Any,
        parent_page: Page | None = None,
        show_locale_labels: bool = False,
        actions_next_url: str | None = None,
        **kwargs: Any,
    ) -> None: ...
    def get_ascending_title_text(self, column: BaseColumn) -> str: ...
    def get_descending_title_text(self, column: BaseColumn) -> str: ...
    def get_row_classname(self, instance: Page) -> str: ...
    def get_row_attrs(self, instance: Page) -> dict[str, str]: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...
