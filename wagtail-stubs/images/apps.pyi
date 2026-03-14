from . import checks as checks, get_image_model as get_image_model
from django.apps import AppConfig

class WagtailImagesAppConfig(AppConfig):
    name: str
    label: str
    verbose_name: str
    default_auto_field: str
    default_attrs: dict[str, str]
    def ready(self) -> None: ...
