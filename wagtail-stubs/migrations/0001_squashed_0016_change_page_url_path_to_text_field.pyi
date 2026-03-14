from _typeshed import Incomplete
from django.db import migrations

def initial_data(apps, schema_editor) -> None: ...
def remove_initial_data(apps, schema_editor) -> None: ...
def set_page_path_collation(apps, schema_editor) -> None: ...

class Migration(migrations.Migration):
    replaces: Incomplete
    dependencies: Incomplete
    operations: Incomplete
