from typing import Any

from django.db import models

class LockableMixin(models.Model):
    locked: models.BooleanField[bool, bool]
    locked_at: models.DateTimeField[Any, Any]
    locked_by: models.ForeignKey[Any, Any]

    class Meta:
        abstract: bool
