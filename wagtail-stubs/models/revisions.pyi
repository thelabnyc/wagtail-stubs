import datetime
from typing import Any, ClassVar, Self

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q
from django.db.models.expressions import Subquery
from django.utils.functional import cached_property

class RevisionQuerySet(models.QuerySet["Revision"]):
    def page_revisions_q(self) -> Q: ...
    def page_revisions(self) -> RevisionQuerySet: ...
    def not_page_revisions(self) -> RevisionQuerySet: ...
    def for_instance(self, instance: models.Model) -> RevisionQuerySet: ...

class RevisionsManager(models.Manager["Revision"]):
    def previous_revision_id_subquery(
        self, revision_fk_name: str = "revision"
    ) -> Subquery: ...

class PageRevisionsManager(RevisionsManager):
    def get_queryset(self) -> RevisionQuerySet: ...

class Revision(models.Model):
    content_type: models.ForeignKey[ContentType, ContentType]
    base_content_type: models.ForeignKey[ContentType, ContentType]
    object_id: models.CharField[str, str]
    created_at: models.DateTimeField[datetime.datetime, datetime.datetime]
    user: models.ForeignKey[AbstractBaseUser | None, AbstractBaseUser | None]
    object_str: models.TextField[str, str]
    content: models.JSONField[dict[str, Any], dict[str, Any]]
    approved_go_live_at: models.DateTimeField[
        datetime.datetime | None, datetime.datetime | None
    ]

    objects: RevisionsManager  # type: ignore[assignment]
    page_revisions: ClassVar[PageRevisionsManager]

    content_object: GenericForeignKey

    wagtail_reference_index_ignore: ClassVar[bool]

    @cached_property
    def base_content_object(self) -> models.Model: ...
    def save(self, user: AbstractBaseUser | None = None, *args: Any, **kwargs: Any) -> None: ...  # type: ignore[override]
    def as_object(self) -> models.Model: ...
    def is_latest_revision(self) -> bool: ...
    def delete(self, using: str | None = None, keep_parents: bool = False) -> tuple[int, dict[str, int]]: ...
    def publish(
        self,
        user: AbstractBaseUser | None = None,
        changed: bool = True,
        log_action: bool = True,
        previous_revision: Revision | None = None,
        skip_permission_checks: bool = False,
    ) -> None: ...
    def get_previous(self) -> Revision: ...
    def get_next(self) -> Revision: ...
    def __str__(self) -> str: ...

    class Meta:
        verbose_name: str
        verbose_name_plural: str

class RevisionMixin(models.Model):
    latest_revision: models.ForeignKey[Revision | None, Revision | None]

    default_exclude_fields_in_copy: ClassVar[list[str]]

    @property
    def revisions(self) -> models.QuerySet[Revision]: ...
    def get_base_content_type(self) -> ContentType: ...
    def get_content_type(self) -> ContentType: ...
    def get_latest_revision(self) -> Revision | None: ...
    def get_latest_revision_as_object(self) -> Self: ...
    def serializable_data(self) -> dict[str, Any]: ...
    @classmethod
    def from_serializable_data(
        cls, data: dict[str, Any], check_fks: bool = True, strict_fks: bool = False
    ) -> Self: ...
    def with_content_json(self, content: dict[str, Any]) -> Self: ...
    def save_revision(
        self,
        user: AbstractBaseUser | None = None,
        approved_go_live_at: datetime.datetime | None = None,
        changed: bool = True,
        log_action: bool | str = False,
        previous_revision: Revision | None = None,
        clean: bool = True,
    ) -> Revision: ...

    class Meta:
        abstract: bool
