from django.db.migrations.operations.base import Operation
from django.db import migrations

def get_image_permissions(apps): ...
def copy_image_permissions_to_collections(apps, schema_editor) -> None: ...
def remove_image_permissions_from_collections(apps, schema_editor) -> None: ...

class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]]
    operations: list[Operation]
