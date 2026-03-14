from django.core.management.base import BaseCommand
from wagtail.contrib.redirects.base_formats import Dataset as Dataset
from wagtail.contrib.redirects.forms import RedirectForm as RedirectForm
from wagtail.contrib.redirects.utils import get_format_cls_by_extension as get_format_cls_by_extension, get_supported_extensions as get_supported_extensions
from wagtail.models import Site as Site

class Command(BaseCommand):
    help: str
    def add_arguments(self, parser) -> None: ...
    def handle(self, *args, **options) -> None: ...

def get_input(msg): ...
