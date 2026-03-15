from typing import Any, Self
import datetime

from django.contrib.auth.models import AbstractBaseUser
from django.core.checks import CheckMessage
from django.db import models
from wagtail.locks import BaseLock

class LockableMixin(models.Model):
    locked: models.BooleanField[bool, bool]
    locked_at: models.DateTimeField[datetime.datetime | None, datetime.datetime | None]
    locked_by: models.ForeignKey[AbstractBaseUser | None, AbstractBaseUser | None]

    class Meta:
        abstract: bool

    @classmethod
    def check(cls, **kwargs: Any) -> list[CheckMessage]: ...
    @classmethod
    def _check_revision_mixin(cls) -> list[CheckMessage]: ...
    def with_content_json(self, content: dict[str, Any]) -> Self: ...
    def get_lock(self) -> BaseLock | None: ...
