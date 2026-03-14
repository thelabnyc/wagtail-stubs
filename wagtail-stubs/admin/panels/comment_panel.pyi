from typing import Any

from .base import Panel

class CommentPanel(Panel):
    def get_form_options(self) -> dict[str, Any]: ...
    @property
    def clean_name(self) -> str: ...

    class BoundPanel(Panel.BoundPanel):
        template_name: str

        def get_context_data(self, parent_context: dict[str, Any] | None = None) -> dict[str, Any]: ...
        def show_panel_furniture(self) -> bool: ...
