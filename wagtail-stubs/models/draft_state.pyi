from typing import Any

from django.db import models

class DraftStateMixin(models.Model):
    live: models.BooleanField[bool, bool]
    has_unpublished_changes: models.BooleanField[bool, bool]
    first_published_at: models.DateTimeField[Any, Any]
    last_published_at: models.DateTimeField[Any, Any]
    live_revision: models.ForeignKey[Any, Any]
    latest_revision: models.ForeignKey[Any, Any]
    go_live_at: models.DateTimeField[Any, Any]
    expire_at: models.DateTimeField[Any, Any]
    expired: models.BooleanField[bool, bool]

    class Meta:
        abstract: bool
