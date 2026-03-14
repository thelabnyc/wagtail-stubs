from typing import Any

from django import forms

from .base import Panel

class FieldPanel(Panel):
    TEMPLATE_VAR: str
    read_only_output_template_name: str
    field_name: str
    widget: type[forms.Widget] | forms.Widget | None
    disable_comments: bool | None
    permission: str | None
    read_only: bool
    required_on_save: bool | None

    def __init__(
        self,
        field_name: str,
        widget: type[forms.Widget] | forms.Widget | None = None,
        disable_comments: bool | None = None,
        permission: str | None = None,
        read_only: bool = False,
        required_on_save: bool | None = None,
        **kwargs: Any,
    ) -> None: ...
    def clone_kwargs(self) -> dict[str, Any]: ...
    def get_form_options(self) -> dict[str, Any]: ...
    def on_model_bound(self) -> None: ...
