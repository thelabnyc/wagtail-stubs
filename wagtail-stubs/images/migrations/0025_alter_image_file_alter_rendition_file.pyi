from collections.abc import Callable

from django.db.migrations.operations.base import Operation

from django.db import migrations

class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]]
    rendition_file_options: dict[str, str | Callable[..., object]]
    operations: list[Operation]
