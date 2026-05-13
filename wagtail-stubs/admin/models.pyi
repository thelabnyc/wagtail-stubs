from typing import Any, ClassVar, Self
import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from wagtail.admin import panels as panels
from wagtail.models.pages import Page as Page

class Admin(models.Model):
    class Meta:
        default_permissions: list[str]
        permissions: list[tuple[str, str]]

def get_object_usage(obj): ...
def popular_tags_for_model(model, count: int = 10): ...

class EditingSessionQuerySet(models.QuerySet["EditingSession"]):
    def stale(self) -> Self: ...
    def available(self) -> Self: ...

class EditingSessionManager(models.Manager["EditingSession"]):
    def get_queryset(self) -> EditingSessionQuerySet: ...
    def stale(self) -> EditingSessionQuerySet: ...
    def available(self) -> EditingSessionQuerySet: ...

class EditingSession(models.Model):
    user: models.ForeignKey[AbstractBaseUser, AbstractBaseUser]
    content_type: models.ForeignKey[ContentType, ContentType]
    object_id: models.CharField[str, str]
    content_object: GenericForeignKey
    last_seen_at: models.DateTimeField[datetime.datetime, datetime.datetime]
    is_editing: models.BooleanField[bool, bool]
    objects: ClassVar[EditingSessionManager]
    IDLE_TIMEOUT: ClassVar[datetime.timedelta]
    AVAILABLE_TIMEOUT: ClassVar[datetime.timedelta]
    STALE_TIMEOUT: ClassVar[datetime.timedelta]
    @classmethod
    def cleanup(cls) -> None: ...
    @property
    def is_idle(self) -> bool: ...
    @property
    def is_available(self) -> bool: ...
    class Meta:
        indexes: list[models.Index]

class FormStateQuerySet(models.QuerySet["FormState"]):
    def for_instance(self, instance: models.Model) -> Self: ...
    def for_preview(
        self,
        user: AbstractBaseUser,
        instance: models.Model,
        parent_object_id: str = "",
    ) -> Self: ...
    def stale(self) -> Self: ...

class FormStateManager(models.Manager["FormState"]):
    def get_queryset(self) -> FormStateQuerySet: ...
    def for_instance(self, instance: models.Model) -> FormStateQuerySet: ...
    def for_preview(
        self,
        user: AbstractBaseUser,
        instance: models.Model,
        parent_object_id: str = "",
    ) -> FormStateQuerySet: ...
    def stale(self) -> FormStateQuerySet: ...
    def update_or_create_by_instance(
        self,
        instance: models.Model,
        parent_object_id: str = "",
        **kwargs: Any,
    ) -> tuple[FormState, bool]: ...

class FormState(models.Model):
    data: models.TextField[str, str]
    user: models.ForeignKey[AbstractBaseUser, AbstractBaseUser]
    content_type: models.ForeignKey[ContentType, ContentType]
    object_id: models.CharField[str, str]
    content_object: GenericForeignKey
    parent_object_id: models.CharField[str, str]
    last_updated_at: models.DateTimeField[datetime.datetime, datetime.datetime]
    objects: ClassVar[FormStateManager]
    STALE_TIMEOUT: ClassVar[datetime.timedelta]
    class Meta:
        indexes: list[models.Index]
        ordering: list[str]
