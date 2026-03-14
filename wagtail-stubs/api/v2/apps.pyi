from _typeshed import Incomplete
from django.apps import AppConfig

class WagtailAPIV2AppConfig(AppConfig):
    name: str
    label: str
    verbose_name: Incomplete
    def ready(self) -> None: ...
