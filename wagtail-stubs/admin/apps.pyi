from . import checks as checks
from django.apps import AppConfig

class WagtailAdminAppConfig(AppConfig):
    name: str
    label: str
    verbose_name: str
    default_auto_field: str
    def ready(self) -> None: ...
