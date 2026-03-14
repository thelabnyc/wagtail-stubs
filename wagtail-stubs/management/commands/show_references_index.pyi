from django.core.management.base import BaseCommand
from wagtail.models import ReferenceIndex as ReferenceIndex

def model_name(model): ...

class Command(BaseCommand):
    def handle(self, **options): ...
