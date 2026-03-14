from typing import Any

from .field_panel import FieldPanel

class TitleFieldPanel(FieldPanel):
    apply_if_live: bool
    def __init__(self, field_name: str, apply_if_live: bool = True, **kwargs: Any) -> None: ...
