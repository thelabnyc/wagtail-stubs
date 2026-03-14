from typing import Any

from .field_panel import FieldPanel

class PageChooserPanel(FieldPanel):
    page_type: list[str | type] | str | type | None
    can_choose_root: bool

    def __init__(
        self,
        field_name: str,
        page_type: list[str | type] | str | type | None = None,
        can_choose_root: bool = False,
        **kwargs: Any,
    ) -> None: ...
    def clone_kwargs(self) -> dict[str, Any]: ...
    def get_form_options(self) -> dict[str, Any]: ...
