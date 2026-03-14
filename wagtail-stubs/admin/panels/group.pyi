from collections.abc import Sequence
from typing import Any

from django.forms import Media

from .base import Panel

class PanelGroup(Panel):
    children: Sequence[Panel]
    permission: str | None
    def __init__(self, children: Sequence[Panel] = (), *args: Any, permission: str | None = None, **kwargs: Any) -> None: ...
    def clone_kwargs(self) -> dict[str, Any]: ...
    def get_form_options(self) -> dict[str, Any]: ...
    def on_model_bound(self) -> None: ...
    @property
    def child_identifiers(self) -> list[str]: ...

    class BoundPanel(Panel.BoundPanel):
        @property
        def children(self) -> list[Panel.BoundPanel]: ...
        @property
        def visible_children(self) -> list[Panel.BoundPanel]: ...
        @property
        def visible_children_with_identifiers(self) -> list[tuple[Panel.BoundPanel, str]]: ...
        def show_panel_furniture(self) -> bool: ...
        def is_shown(self) -> bool: ...
        @property
        def media(self) -> Media: ...
        def get_comparison(self) -> list[Any]: ...

class TabbedInterface(PanelGroup):
    class BoundPanel(PanelGroup.BoundPanel):
        template_name: str

class ObjectList(PanelGroup):
    class BoundPanel(PanelGroup.BoundPanel):
        template_name: str

class FieldRowPanel(PanelGroup):
    class BoundPanel(PanelGroup.BoundPanel):
        template_name: str

class MultiFieldPanel(PanelGroup):
    class BoundPanel(PanelGroup.BoundPanel):
        template_name: str
