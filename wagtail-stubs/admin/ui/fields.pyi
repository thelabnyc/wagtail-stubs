from typing import Any

from django.db import models
from wagtail.admin.ui.components import Component as Component
from wagtail.utils.registry import ModelFieldRegistry as ModelFieldRegistry

display_class_registry: ModelFieldRegistry

def register_display_class(field_class: type[models.Field], to: type[models.Model] | None = None, display_class: type[BaseFieldDisplay] | None = None, exact_class: bool = False) -> None: ...

class BaseFieldDisplay(Component):
    value: Any
    def __init__(self, value: Any) -> None: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...
