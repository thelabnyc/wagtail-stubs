from typing import Any

from django.core.management.base import BaseCommand
from django.db import models
from wagtail.models.reference_index import ReferenceIndex as ReferenceIndex

def model_name(model: type[models.Model]) -> str: ...

class Command(BaseCommand):
    def handle(self, **options: Any) -> None: ...
