from _typeshed import Incomplete
from django.db import migrations

def get_document_permissions(apps): ...
def copy_document_permissions_to_collections(apps, schema_editor) -> None: ...
def remove_document_permissions_from_collections(apps, schema_editor) -> None: ...

class Migration(migrations.Migration):
    dependencies: Incomplete
    operations: Incomplete
