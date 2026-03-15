from django import forms

from .field_panel import FieldPanel

class PageChooserPanel(FieldPanel):
    page_type: list[str | type] | str | type | None
    can_choose_root: bool

    def __init__(
        self,
        field_name: str,
        page_type: list[str | type] | str | type | None = None,
        can_choose_root: bool = False,
        **kwargs: str | type[forms.Widget] | forms.Widget | bool | dict[str, str] | None,
    ) -> None: ...
    def clone_kwargs(self) -> dict[str, str | list[str | type] | type | bool | forms.Widget | type[forms.Widget] | None]: ...
    def get_form_options(self) -> dict[str, list[str] | dict[str, str | forms.Widget | type[forms.Widget]]]: ...
