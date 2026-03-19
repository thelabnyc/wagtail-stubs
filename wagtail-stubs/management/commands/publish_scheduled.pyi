from django.core.management.base import BaseCommand
from wagtail.models.draft_state import DraftStateMixin as DraftStateMixin
from wagtail.models.pages import Page as Page
from wagtail.models.revisions import Revision as Revision

def revision_date_expired(r): ...

class Command(BaseCommand):
    def add_arguments(self, parser) -> None: ...
    def handle(self, *args, **options) -> None: ...
