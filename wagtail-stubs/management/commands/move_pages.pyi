from django.core.management.base import BaseCommand
from wagtail.models import AbstractPage

Page: type[AbstractPage]

class Command(BaseCommand):
    def add_arguments(self, parser) -> None: ...
    def handle(self, *args, **options) -> None: ...
