from django.db import migrations
from django.db.migrations.operations.base import Operation

class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]]
    operations: list[Operation]
