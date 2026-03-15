from django.core.management.base import BaseCommand
from wagtail.models import (
    BaseLogEntry as BaseLogEntry,
)
from wagtail.models import (
    BootstrapTranslatableMixin as BootstrapTranslatableMixin,
)
from wagtail.models import (
    ReferenceIndex as ReferenceIndex,
)
from wagtail.models import (
    TranslatableMixin as TranslatableMixin,
)

class Command(BaseCommand):
    help: str
    def convert_field(self, model, field_name, null: bool = False) -> None: ...
    def handle(self, **options) -> None: ...
