from collections.abc import Callable

from django.db import migrations
from django.db.migrations.operations.base import Operation

class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]]
    rendition_file_options: dict[str, str | Callable[..., object]]
    operations: list[Operation]
