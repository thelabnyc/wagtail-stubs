from _typeshed import Incomplete
from wagtail.admin.ui.components import Component as Component
from wagtail.utils.registry import ModelFieldRegistry as ModelFieldRegistry

display_class_registry: Incomplete

def register_display_class(field_class, to=None, display_class=None, exact_class: bool = False) -> None: ...

class BaseFieldDisplay(Component):
    value: Incomplete
    def __init__(self, value) -> None: ...
    def get_context_data(self, parent_context): ...
