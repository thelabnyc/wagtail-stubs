from django.apps import AppConfig
from django.utils.functional import _StrOrPromise

class WagtailTableBlockAppConfig(AppConfig):
    name: str
    label: str
    verbose_name: _StrOrPromise
    def ready(self) -> None: ...
