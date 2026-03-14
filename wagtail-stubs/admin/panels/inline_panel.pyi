from typing import Any

from django.utils.functional import cached_property

from .base import Panel

class InlinePanel(Panel):
    relation_name: str
    panels: list[Panel] | None
    label: str
    min_num: int | None
    max_num: int | None
    db_field: Any

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
    def clone_kwargs(self) -> dict[str, Any]: ...
    @cached_property
    def panel_definitions(self) -> list[Panel]: ...
    @cached_property
    def child_edit_handler(self) -> Panel: ...
    def get_form_options(self) -> dict[str, Any]: ...
    def on_model_bound(self) -> None: ...
    def classes(self) -> list[str]: ...

    class BoundPanel(Panel.BoundPanel):
        template_name: str
        label: str
        formset: Any
        child_edit_handler: Panel
        children: list[Any]
        empty_child: Any

        def __init__(self, **kwargs: Any) -> None: ...
        def get_comparison(self) -> list[Any]: ...
        def get_context_data(self, parent_context: dict[str, Any] | None = None) -> dict[str, Any]: ...
