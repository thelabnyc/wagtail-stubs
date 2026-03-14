from django.core.management.base import BaseCommand
from wagtail.contrib.search_promotions import models as models

class Command(BaseCommand):
    def handle(self, **options) -> None: ...
