import datetime
import uuid
from typing import Any, Iterator

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.functional import cached_property

from wagtail.log_actions import LogFormatter
from wagtail.models.revisions import Revision

class LogEntryQuerySet(models.QuerySet["BaseLogEntry"]):
    def get_actions(self) -> set[str]: ...
    def get_user_ids(self) -> set[int]: ...
    def get_users(self) -> models.QuerySet[AbstractBaseUser]: ...
    def get_content_type_ids(self) -> set[int]: ...
    def filter_on_content_type(
        self, content_type: ContentType
    ) -> LogEntryQuerySet: ...
    def with_instances(
        self,
    ) -> Iterator[tuple[BaseLogEntry, models.Model | None]]: ...

class BaseLogEntryManager(models.Manager["BaseLogEntry"]):
    def get_queryset(self) -> LogEntryQuerySet: ...
    def get_instance_title(self, instance: models.Model) -> str: ...
    def log_action(
        self, instance: models.Model, action: str, **kwargs: Any
    ) -> BaseLogEntry: ...
    def viewable_by_user(self, user: AbstractBaseUser) -> LogEntryQuerySet: ...
    def get_for_model(self, model: type[models.Model]) -> LogEntryQuerySet: ...
    def get_for_user(self, user_id: int) -> LogEntryQuerySet: ...
    def for_instance(self, instance: models.Model) -> LogEntryQuerySet: ...

class BaseLogEntry(models.Model):
    content_type: models.ForeignKey[ContentType | None, ContentType | None]
    label: models.TextField[str, str]
    action: models.CharField[str, str]
    data: models.JSONField[dict[str, Any], dict[str, Any]]
    timestamp: models.DateTimeField[datetime.datetime, datetime.datetime]
    uuid: models.UUIDField[uuid.UUID | None, uuid.UUID | str | None]
    user: models.ForeignKey[AbstractBaseUser | None, AbstractBaseUser | None]
    revision: models.ForeignKey[Revision | None, Revision | None]
    content_changed: models.BooleanField[bool, bool]
    deleted: models.BooleanField[bool, bool]
    objects: BaseLogEntryManager  # type: ignore[assignment]
    wagtail_reference_index_ignore: bool

    class Meta:
        abstract: bool
        verbose_name: str
        verbose_name_plural: str
        ordering: list[str]

    def save(self, *args: Any, **kwargs: Any) -> None: ...
    def clean(self) -> None: ...
    @cached_property
    def user_display_name(self) -> str: ...
    @cached_property
    def object_verbose_name(self) -> str: ...
    def object_id(self) -> str: ...
    @cached_property
    def formatter(self) -> LogFormatter | None: ...
    @cached_property
    def message(self) -> str: ...
    @cached_property
    def comment(self) -> str: ...

class ModelLogEntryManager(BaseLogEntryManager):
    def log_action(  # type: ignore[override]
        self, instance: models.Model, action: str, **kwargs: Any
    ) -> ModelLogEntry: ...
    def for_instance(self, instance: models.Model) -> LogEntryQuerySet: ...

class ModelLogEntry(BaseLogEntry):
    object_id: models.CharField[str, str]  # type: ignore[assignment]
    objects: ModelLogEntryManager  # type: ignore[assignment]

    class Meta:
        ordering: list[str]
        verbose_name: str
        verbose_name_plural: str
