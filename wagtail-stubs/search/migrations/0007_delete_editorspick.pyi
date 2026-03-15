from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations.state import ProjectState
from django.db.migrations.operations.base import Operation

from django.db import migrations

class DeleteModelIfExists(migrations.DeleteModel):
    def database_forwards(self, app_label: str, schema_editor: BaseDatabaseSchemaEditor, from_state: ProjectState, to_state: ProjectState) -> None: ...

class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]]
    operations: list[Operation]
