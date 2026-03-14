from django.core.management.base import BaseCommand
from wagtail.models import BaseLogEntry as BaseLogEntry, BootstrapTranslatableMixin as BootstrapTranslatableMixin, ReferenceIndex as ReferenceIndex, TranslatableMixin as TranslatableMixin

class Command(BaseCommand):
    help: str
    def convert_field(self, model, field_name, null: bool = False) -> None: ...
    def handle(self, **options) -> None: ...
