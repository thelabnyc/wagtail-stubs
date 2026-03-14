from .finders import get_finders as get_finders
from django.apps import AppConfig

class WagtailEmbedsAppConfig(AppConfig):
    name: str
    label: str
    verbose_name: str
    default_auto_field: str
    def ready(self) -> None: ...
