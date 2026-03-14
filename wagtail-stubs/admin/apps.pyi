from . import checks as checks
from _typeshed import Incomplete
from django.apps import AppConfig

class WagtailAdminAppConfig(AppConfig):
    name: str
    label: str
    verbose_name: Incomplete
    default_auto_field: str
    def ready(self) -> None: ...
