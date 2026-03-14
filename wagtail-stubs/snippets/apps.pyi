from _typeshed import Incomplete
from django.apps import AppConfig

class WagtailSnippetsAppConfig(AppConfig):
    name: str
    label: str
    verbose_name: Incomplete
    def ready(self) -> None: ...
