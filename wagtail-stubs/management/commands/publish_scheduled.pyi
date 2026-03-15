from django.core.management.base import BaseCommand
from wagtail.models import DraftStateMixin as DraftStateMixin
from wagtail.models import Page as Page
from wagtail.models import Revision as Revision

def revision_date_expired(r): ...

class Command(BaseCommand):
    def add_arguments(self, parser) -> None: ...
    def handle(self, *args, **options) -> None: ...
