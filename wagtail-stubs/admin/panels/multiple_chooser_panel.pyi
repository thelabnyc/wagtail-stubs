from typing import Any

from django.forms import Media

from .inline_panel import InlinePanel

class MultipleChooserPanel(InlinePanel):
    chooser_field_name: str

    def __init__(
        self,
        relation_name: str,
        chooser_field_name: str | None = None,
        **kwargs: Any,
    ) -> None: ...
    def clone_kwargs(self) -> dict[str, Any]: ...

    class BoundPanel(InlinePanel.BoundPanel):
        template_name: str
        chooser_widget: Any
        js_context: Any
        chooser_widget_telepath_definition: Any

        def __init__(self, *args: Any, **kwargs: Any) -> None: ...
        def get_context_data(self, parent_context: dict[str, Any] | None = None) -> dict[str, Any]: ...
        @property
        def media(self) -> Media: ...
