from django.db.migrations.operations.base import Operation
from django.db import migrations
from wagtail.embeds.embeds import get_embed_hash as get_embed_hash

def migrate_forwards(apps, schema_editor) -> None: ...

class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]]
    operations: list[Operation]
