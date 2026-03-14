from typing import Any

from .inline_panel import InlinePanel

class MultipleChooserPanel(InlinePanel):
    chooser_field_name: str | None
    def __init__(self, relation_name: str, chooser_field_name: str | None = None, **kwargs: Any) -> None: ...
