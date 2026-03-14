from typing import Any

from django.db import migrations

class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]]
    rendition_file_options: dict[str, Any]
    operations: list[Any]
