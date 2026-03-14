from typing import Any

from .base import Panel

class HelpPanel(Panel):
    content: str
    template: str

    def __init__(
        self,
        content: str = "",
        template: str = "wagtailadmin/panels/help_panel.html",
        **kwargs: Any,
    ) -> None: ...
    def clone_kwargs(self) -> dict[str, Any]: ...
    @property
    def clean_name(self) -> str: ...

    class BoundPanel(Panel.BoundPanel):
        template_name: str
        content: str

        def __init__(self, **kwargs: Any) -> None: ...
