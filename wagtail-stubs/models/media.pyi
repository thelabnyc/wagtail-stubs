from typing import ClassVar

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import ForeignKey
from django.utils.safestring import SafeString
from treebeard.mp_tree import MP_Node
from wagtail.query import TreeQuerySet
from wagtail.search import index

from .view_restrictions import BaseViewRestriction

class CollectionQuerySet(TreeQuerySet):
    def get_min_depth(self) -> int: ...
    def get_indented_choices(self) -> list[tuple[int, str | SafeString]]: ...

class BaseCollectionManager(models.Manager["Collection"]):
    def get_queryset(self) -> CollectionQuerySet: ...

class CollectionManager(BaseCollectionManager, CollectionQuerySet):  # type: ignore[misc]
    ...

class CollectionViewRestriction(BaseViewRestriction):
    collection: ForeignKey[Collection, Collection]
    passed_view_restrictions_session_key: str

    class Meta:
        verbose_name: str
        verbose_name_plural: str

class Collection(MP_Node):
    name: models.CharField[str, str]
    objects: ClassVar[CollectionManager]  # type: ignore[assignment]
    node_order_by: ClassVar[list[str]]

    def get_ancestors(self, inclusive: bool = False) -> CollectionQuerySet: ...
    def get_descendants(self, inclusive: bool = False) -> CollectionQuerySet: ...
    def get_siblings(self, inclusive: bool = True) -> CollectionQuerySet: ...
    def get_next_siblings(self, inclusive: bool = False) -> CollectionQuerySet: ...
    def get_prev_siblings(self, inclusive: bool = False) -> CollectionQuerySet: ...
    def get_view_restrictions(self) -> models.QuerySet[CollectionViewRestriction]: ...
    def get_indented_name(self, indentation_start_depth: int = 2, html: bool = False) -> str | SafeString: ...

    class Meta:
        verbose_name: str
        verbose_name_plural: str

def get_root_collection_id() -> int: ...

class CollectionMember(models.Model):
    collection: ForeignKey[Collection, Collection]
    search_fields: ClassVar[list[index.FilterField]]

    class Meta:
        abstract: bool

class GroupCollectionPermissionManager(models.Manager["GroupCollectionPermission"]):
    def get_by_natural_key(self, group: str, collection: str, permission: str) -> GroupCollectionPermission: ...

class GroupCollectionPermission(models.Model):
    group: ForeignKey[Group, Group]
    collection: ForeignKey[Collection, Collection]
    permission: ForeignKey[Permission, Permission]
    objects: ClassVar[GroupCollectionPermissionManager]  # type: ignore[assignment]

    def natural_key(self) -> tuple[Group, Collection, Permission]: ...

    class Meta:
        unique_together: tuple[tuple[str, ...]]
        verbose_name: str
        verbose_name_plural: str

class UploadedFile(models.Model):
    for_content_type: ForeignKey[ContentType | None, ContentType | None]
    file: models.FileField
    uploaded_by_user: ForeignKey[models.Model | None, models.Model | None]
