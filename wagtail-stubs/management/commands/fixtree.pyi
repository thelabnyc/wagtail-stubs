from typing import Any

from django.core.management.base import BaseCommand
from wagtail.models.media import Collection as Collection
from wagtail.models.pages import Page as Page

class Command(BaseCommand):
    help: str
    stealth_options: tuple[str, ...]
    def add_arguments(self, parser: Any) -> None: ...
    def numberlist_to_string(self, numberlist: list[int]) -> str: ...
    def handle(self, **options: Any) -> None: ...
    def handle_model(
        self, model: type, model_name: str, model_name_plural: str, any_problems_fixed: bool, options: dict[str, Any]
    ) -> None: ...
