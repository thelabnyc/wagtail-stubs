from collections.abc import Generator, Iterable
from typing import Any

from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import QuerySet
from wagtail.models.reference_index import ReferenceIndex as ReferenceIndex
from wagtail.signal_handlers import disable_reference_index_auto_update as disable_reference_index_auto_update

DEFAULT_CHUNK_SIZE: int

class Command(BaseCommand):
    def write(self, *args: Any, **kwargs: Any) -> None: ...
    def add_arguments(self, parser: Any) -> None: ...
    verbosity: int
    def handle(self, **options: Any) -> None: ...
    def print_newline(self) -> None: ...
    def print_iter_progress(self, iterable: Iterable[Any]) -> Generator[Any]: ...
    @transaction.atomic
    def queryset_chunks(self, qs: QuerySet[Any], chunk_size: int = ...) -> Generator[list[Any]]: ...
