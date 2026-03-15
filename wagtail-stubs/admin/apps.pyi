from django.apps import AppConfig

from . import checks as checks

class WagtailAdminAppConfig(AppConfig):
    name: str
    label: str
    verbose_name: str
    default_auto_field: str
    def ready(self) -> None: ...
