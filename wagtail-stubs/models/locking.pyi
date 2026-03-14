import datetime
from typing import Any, Self

from django.contrib.auth.models import AbstractBaseUser
from django.core.checks import Error
from django.db import models

from wagtail.locks import BasicLock

class LockableMixin(models.Model):
    locked: models.BooleanField[bool, bool]
    locked_at: models.DateTimeField[datetime.datetime | None, datetime.datetime | None]
    locked_by: models.ForeignKey[AbstractBaseUser | None, AbstractBaseUser | None]

    class Meta:
        abstract: bool

    @classmethod
    def check(cls, **kwargs: Any) -> list[Error]: ...
    @classmethod
    def _check_revision_mixin(cls) -> list[Error]: ...
    def with_content_json(self, content: Any) -> Self: ...
    def get_lock(self) -> BasicLock | None: ...
