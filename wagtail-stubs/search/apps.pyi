from typing import Any

from django.apps import AppConfig

class WagtailSearchAppConfig(AppConfig):
    name: str
    label: str
    verbose_name: str
    default_auto_field: str
    def ready(self) -> None: ...
