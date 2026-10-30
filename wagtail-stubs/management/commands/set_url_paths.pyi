from django.core.management.base import BaseCommand
from wagtail.models import AbstractPage

Page: type[AbstractPage]

class Command(BaseCommand):
    help: str
    def set_subtree(self, root, parent=None) -> None: ...
    def handle(self, *args, **options) -> None: ...
