from django.apps import AppConfig

class WagtailSnippetsAppConfig(AppConfig):
    name: str
    label: str
    verbose_name: str
    def ready(self) -> None: ...
