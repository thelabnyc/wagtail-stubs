from django.db import migrations
from django.db.migrations.operations.base import Operation

def remove_duplicate_renditions(apps, schema_editor) -> None: ...
def reverse_remove_duplicate_renditions(*args, **kwargs) -> None: ...

class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]]
    operations: list[Operation]
