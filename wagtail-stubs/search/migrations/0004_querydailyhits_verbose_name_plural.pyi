from django.db.migrations.operations.base import Operation

from django.db import migrations

class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]]
    operations: list[Operation]
