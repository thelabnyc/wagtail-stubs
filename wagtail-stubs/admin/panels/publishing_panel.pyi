from collections.abc import Sequence
from typing import Any

from django.forms import Form

from .base import Panel
from .group import MultiFieldPanel

class PublishingPanel(MultiFieldPanel):
    def __init__(self, **kwargs: str | Sequence[Panel] | type[Form] | dict[str, str] | None) -> None: ...
    @property
    def clean_name(self) -> str: ...

    class BoundPanel(MultiFieldPanel.BoundPanel):
        template_name: str

        def get_context_data(self, parent_context: dict[str, Any] | None = None) -> dict[str, Any]: ...
        def show_panel_furniture(self) -> bool: ...
