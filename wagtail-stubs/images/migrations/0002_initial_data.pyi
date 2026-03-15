from django.db import migrations
from django.db.migrations.operations.base import Operation

def add_image_permissions_to_admin_groups(apps, schema_editor) -> None: ...
def remove_image_permissions(apps, schema_editor) -> None: ...

class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]]
    operations: list[Operation]
