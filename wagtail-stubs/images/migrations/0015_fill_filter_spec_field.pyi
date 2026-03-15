from collections.abc import Callable

from django.apps.registry import Apps
from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations.operations.base import Operation
from wagtail.images.utils import get_fill_filter_spec_migrations as get_fill_filter_spec_migrations

class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]]
    forward: Callable[[Apps, BaseDatabaseSchemaEditor], None]
    reverse: Callable[[Apps, BaseDatabaseSchemaEditor], None]
    operations: list[Operation]
