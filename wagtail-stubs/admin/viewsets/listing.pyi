from collections.abc import Sequence
from typing import Any

from wagtail.admin.filters import WagtailFilterSet
from wagtail.admin.ui.tables import BaseColumn
from wagtail.admin.viewsets.base import _Undefined

type ListDisplayItem = str | BaseColumn
type ListFilter = list[str] | tuple[str, ...] | dict[str, Sequence[str]]

class ListingViewSetMixin:
    list_per_page: int | _Undefined
    ordering: str | Sequence[str] | None | _Undefined
    list_display: Sequence[ListDisplayItem] | _Undefined
    list_filter: ListFilter | None | _Undefined
    filterset_class: type[WagtailFilterSet] | None | _Undefined
    list_export: Sequence[str] | _Undefined
    export_headings: dict[str, str] | _Undefined
    export_filename: str | _Undefined
    def get_index_view_kwargs(self, **kwargs: Any) -> dict[str, Any]: ...
