from . import checks as checks, get_image_model as get_image_model
from _typeshed import Incomplete
from django.apps import AppConfig

class WagtailImagesAppConfig(AppConfig):
    name: str
    label: str
    verbose_name: Incomplete
    default_auto_field: str
    default_attrs: Incomplete
    def ready(self) -> None: ...
