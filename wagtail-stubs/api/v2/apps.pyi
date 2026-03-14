from django.apps import AppConfig

class WagtailAPIV2AppConfig(AppConfig):
    name: str
    label: str
    verbose_name: str
    def ready(self) -> None: ...
