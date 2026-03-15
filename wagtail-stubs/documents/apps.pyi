from django.apps import AppConfig

from . import get_document_model as get_document_model

class WagtailDocsAppConfig(AppConfig):
    name: str
    label: str
    verbose_name: str
    default_auto_field: str
    def ready(self) -> None: ...
