from typing import Any, Self
import datetime

from django.contrib.auth.models import AbstractBaseUser
from django.core.checks import CheckMessage
from django.db import models
from django.utils.functional import _StrPromise, cached_property
from wagtail.locks import BaseLock
from wagtail.models.revisions import Revision

class DraftStateMixin(models.Model):
    live: models.BooleanField[bool, bool]
    has_unpublished_changes: models.BooleanField[bool, bool]
    first_published_at: models.DateTimeField[datetime.datetime | None, datetime.datetime | None]
    last_published_at: models.DateTimeField[datetime.datetime | None, datetime.datetime | None]
    live_revision: models.ForeignKey[Revision | None, Revision | None]
    go_live_at: models.DateTimeField[datetime.datetime | None, datetime.datetime | None]
    expire_at: models.DateTimeField[datetime.datetime | None, datetime.datetime | None]
    expired: models.BooleanField[bool, bool]

    class Meta:
        abstract: bool

    @classmethod
    def check(cls, **kwargs: Any) -> list[CheckMessage]: ...
    @classmethod
    def _check_revision_mixin(cls) -> list[CheckMessage]: ...
    @property
    def approved_schedule(self) -> bool: ...
    @property
    def status_string(self) -> _StrPromise: ...
    def publish(
        self,
        revision: Revision,
        user: AbstractBaseUser | None = None,
        changed: bool = True,
        log_action: bool = True,
        previous_revision: Revision | None = None,
        skip_permission_checks: bool = False,
    ) -> None: ...
    def unpublish(
        self,
        set_expired: bool = False,
        commit: bool = True,
        user: AbstractBaseUser | None = None,
        log_action: bool = True,
    ) -> None: ...
    def with_content_json(self, content: dict[str, Any]) -> Self: ...
    def get_latest_revision_as_object(self) -> Self: ...
    @cached_property
    def scheduled_revision(self) -> Revision | None: ...
    def get_scheduled_revision_as_object(self) -> Self | None: ...
    def _update_from_revision(self, revision: Revision, changed: bool = True) -> None: ...
    def get_lock(self) -> BaseLock | None: ...
