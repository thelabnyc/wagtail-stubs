from typing import Any

from .base import Panel

class InlinePanel(Panel):
    relation_name: str
    panels: list[Panel] | None
    label: str
    min_num: int | None
    max_num: int | None
    def __init__(
        self,
        relation_name: str,
        panels: list[Panel] | None = None,
        heading: str = "",
        label: str = "",
        min_num: int | None = None,
        max_num: int | None = None,
        **kwargs: Any,
    ) -> None: ...
    def clone_kwargs(self) -> dict[str, Any]: ...
    def get_form_options(self) -> dict[str, Any]: ...
    def on_model_bound(self) -> None: ...
