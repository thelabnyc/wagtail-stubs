from django.core.management.base import BaseCommand
from wagtail.embeds.models import Embed as Embed

class Command(BaseCommand):
    help: str
    def handle(self, *args, **options) -> None: ...
