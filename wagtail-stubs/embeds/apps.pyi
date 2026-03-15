from django.apps import AppConfig

from .finders import get_finders as get_finders

class WagtailEmbedsAppConfig(AppConfig):
    name: str
    label: str
    verbose_name: str
    default_auto_field: str
    def ready(self) -> None: ...
