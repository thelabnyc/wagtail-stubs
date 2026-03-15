from django.db import migrations
from django.db.migrations.operations.base import Operation
from wagtail.search.backends.database.sqlite.utils import fts5_available as fts5_available
from wagtail.search.models import IndexEntry as IndexEntry

class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]]
    operations: list[Operation]
