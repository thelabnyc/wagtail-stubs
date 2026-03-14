from typing import Any

from django.db import migrations
from wagtail.images.utils import get_fill_filter_spec_migrations as get_fill_filter_spec_migrations

class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]]
    forward: Any
    reverse: Any
    operations: list[Any]
