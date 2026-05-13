from typing import Any

from django.utils.functional import _StrPromise, cached_property
from wagtail.admin.ui.tables import BaseColumn

class OrderingColumn(BaseColumn):
    header_template_name: str
    cell_template_name: str

class OrderableTableMixin:
    success_message: str | _StrPromise
    sort_order_field: str | None
    reorder_url: str | None
    def __init__(
        self,
        *args: Any,
        sort_order_field: str | None = None,
        reorder_url: str | None = None,
        **kwargs: Any,
    ) -> None: ...
    @cached_property
    def ordering_column(self) -> OrderingColumn: ...
    def _add_ordering_column(self) -> None: ...
    @property
    def attrs(self) -> dict[str, str]: ...
    def get_success_message(self) -> str: ...
    def get_row_attrs(self, instance: Any) -> dict[str, str]: ...
    def get_caption(self) -> str | None: ...
