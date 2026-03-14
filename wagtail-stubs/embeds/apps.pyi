from .finders import get_finders as get_finders
from _typeshed import Incomplete
from django.apps import AppConfig

class WagtailEmbedsAppConfig(AppConfig):
    name: str
    label: str
    verbose_name: Incomplete
    default_auto_field: str
    def ready(self) -> None: ...
