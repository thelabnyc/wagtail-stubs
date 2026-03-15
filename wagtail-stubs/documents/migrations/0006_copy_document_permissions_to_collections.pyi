from django.db import migrations
from django.db.migrations.operations.base import Operation

def get_document_permissions(apps): ...
def copy_document_permissions_to_collections(apps, schema_editor) -> None: ...
def remove_document_permissions_from_collections(apps, schema_editor) -> None: ...

class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]]
    operations: list[Operation]
