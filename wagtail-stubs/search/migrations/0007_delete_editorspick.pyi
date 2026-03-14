from _typeshed import Incomplete
from django.db import migrations

class DeleteModelIfExists(migrations.DeleteModel):
    def database_forwards(self, app_label, schema_editor, from_state, to_state) -> None: ...

class Migration(migrations.Migration):
    dependencies: Incomplete
    operations: Incomplete
