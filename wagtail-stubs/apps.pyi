from django.apps import AppConfig

class WagtailAppConfig(AppConfig):
    name: str
    label: str
    verbose_name: str
    default_auto_field: str
    def ready(self) -> None: ...
