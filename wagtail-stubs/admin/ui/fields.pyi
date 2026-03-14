from typing import Any

from wagtail.admin.ui.components import Component as Component
from wagtail.utils.registry import ModelFieldRegistry as ModelFieldRegistry

display_class_registry: ModelFieldRegistry

def register_display_class(field_class, to=None, display_class=None, exact_class: bool = False) -> None: ...

class BaseFieldDisplay(Component):
    value: Any
    def __init__(self, value) -> None: ...
    def get_context_data(self, parent_context): ...
