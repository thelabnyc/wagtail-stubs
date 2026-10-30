from django.apps import AppConfig

class WagtailAPIV3AppConfig(AppConfig):
    name: str
    label: str
    verbose_name: str
    def ready(self) -> None: ...
