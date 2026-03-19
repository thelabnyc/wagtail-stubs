from django.core.management.base import BaseCommand
from wagtail.models.audit_log import BaseLogEntry as BaseLogEntry
from wagtail.models.i18n import BootstrapTranslatableMixin as BootstrapTranslatableMixin
from wagtail.models.i18n import TranslatableMixin as TranslatableMixin
from wagtail.models.reference_index import ReferenceIndex as ReferenceIndex

class Command(BaseCommand):
    help: str
    def convert_field(self, model, field_name, null: bool = False) -> None: ...
    def handle(self, **options) -> None: ...
