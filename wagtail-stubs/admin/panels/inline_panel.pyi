import functools
from typing import Any

from django.db.models.fields.reverse_related import ForeignObjectRel
from django.forms.formsets import BaseFormSet
from django.forms.forms import BaseForm
from django.utils.functional import cached_property

from wagtail.admin.compare import ChildRelationComparison

from .base import Panel

class InlinePanel(Panel):
    relation_name: str
    panels: list[Panel] | None
    label: str
    min_num: int | None
    max_num: int | None
    db_field: ForeignObjectRel

    def __init__(
        self,
        relation_name: str,
        panels: list[Panel] | None = None,
        heading: str = "",
        label: str = "",
        min_num: int | None = None,
        max_num: int | None = None,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def clone_kwargs(self) -> dict[str, str | list[Panel] | int | None]: ...
    @cached_property
    def panel_definitions(self) -> list[Panel]: ...
    @cached_property
    def child_edit_handler(self) -> Panel: ...
    def get_form_options(self) -> dict[str, dict[str, dict[str, list[str] | dict[str, str] | int | bool | type | None]]]: ...
    def on_model_bound(self) -> None: ...
    def classes(self) -> list[str]: ...

    class BoundPanel(Panel.BoundPanel):
        template_name: str
        label: str
        formset: BaseFormSet[BaseForm]
        child_edit_handler: Panel
        children: list[Panel.BoundPanel]
        empty_child: Panel.BoundPanel

        def __init__(self, **kwargs: Any) -> None: ...
        def get_comparison(self) -> list[functools.partial[ChildRelationComparison]]: ...
        def get_context_data(self, parent_context: dict[str, Any] | None = None) -> dict[str, Any]: ...
