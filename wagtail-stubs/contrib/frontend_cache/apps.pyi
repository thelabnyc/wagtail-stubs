from _typeshed import Incomplete
from django.apps import AppConfig
from wagtail.contrib.frontend_cache.signal_handlers import register_signal_handlers as register_signal_handlers

class WagtailFrontendCacheAppConfig(AppConfig):
    name: str
    label: str
    verbose_name: Incomplete
    def ready(self) -> None: ...
