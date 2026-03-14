from typing import Any

from django.db import migrations

class DeleteModelIfExists(migrations.DeleteModel):
    def database_forwards(self, app_label: str, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...

class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]]
    operations: list[Any]
