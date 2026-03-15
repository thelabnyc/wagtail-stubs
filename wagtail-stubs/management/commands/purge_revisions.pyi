from typing import Any

from django.core.management.base import BaseCommand
from wagtail.models import Revision as Revision
from wagtail.models import WorkflowState as WorkflowState

class Command(BaseCommand):
    help: str
    def add_arguments(self, parser: Any) -> None: ...
    def handle(self, *args: Any, **options: Any) -> None: ...

def purge_revisions(days: int | None = None, pages: bool = True, non_pages: bool = True) -> tuple[int, int]: ...
