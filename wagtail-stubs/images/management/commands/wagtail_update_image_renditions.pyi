import logging
from django.core.management.base import BaseCommand
from wagtail.images import get_image_model as get_image_model

logger: logging.Logger

def progress_bar(current, total, bar_length: int = 50): ...

class Command(BaseCommand):
    help: str
    def add_arguments(self, parser) -> None: ...
    def handle(self, *args, **options) -> None: ...
