from typing import Any

from .base import Panel

class HelpPanel(Panel):
    content: str
    template: str
    def __init__(self, content: str = "", template: str = "wagtailadmin/panels/help_panel.html", **kwargs: Any) -> None: ...
    def clone_kwargs(self) -> dict[str, Any]: ...
