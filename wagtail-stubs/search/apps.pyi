from _typeshed import Incomplete
from modelsearch.apps import ModelSearchAppConfig

class WagtailSearchAppConfig(ModelSearchAppConfig):
    name: str
    label: str
    verbose_name: Incomplete
    backend_setting_name: str
    default: bool
