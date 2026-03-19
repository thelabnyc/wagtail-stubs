from typing import Any

from django import forms

from .field_panel import FieldPanel

class TitleFieldPanel(FieldPanel):
    apply_if_live: bool
    placeholder: bool | str
    targets: list[str] | None

    def __init__(
        self,
        *args: str | forms.Widget | type[forms.Widget] | bool | None,
        apply_if_live: bool = False,
        classname: str = "title",
        placeholder: bool | str = True,
        targets: list[str] | None = None,
        **kwargs: str | type[forms.Form] | dict[str, str] | None,
    ) -> None: ...
    def clone_kwargs(self) -> dict[str, str | bool | list[str] | type[forms.Widget] | forms.Widget | None]: ...

    class BoundPanel(FieldPanel.BoundPanel):
        apply_actions: list[str]

        def get_context_data(self, parent_context: dict[str, Any] | None = None) -> dict[str, Any]: ...
        def get_attrs(self) -> dict[str, str]: ...
        def get_placeholder(self) -> str | None: ...
        def get_should_apply(self) -> bool: ...
        def get_target_selector(self, target: str) -> str: ...
