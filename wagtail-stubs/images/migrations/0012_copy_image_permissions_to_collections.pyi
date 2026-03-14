from typing import Any
from django.db import migrations

def get_image_permissions(apps): ...
def copy_image_permissions_to_collections(apps, schema_editor) -> None: ...
def remove_image_permissions_from_collections(apps, schema_editor) -> None: ...

class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]]
    operations: list[Any]
