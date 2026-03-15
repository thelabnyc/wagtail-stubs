from django.apps import AppConfig

from . import checks as checks
from . import get_image_model as get_image_model

class WagtailImagesAppConfig(AppConfig):
    name: str
    label: str
    verbose_name: str
    default_auto_field: str
    default_attrs: dict[str, str]
    def ready(self) -> None: ...
