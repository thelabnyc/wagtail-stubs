from collections.abc import Generator
from contextlib import contextmanager
from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.files.base import File
from django.db import models
from django.dispatch import Signal
from taggit.managers import TaggableManager
from wagtail.models.media import CollectionMember as CollectionMember
from wagtail.models.reference_index import ReferenceGroups
from wagtail.models.reference_index import ReferenceIndex as ReferenceIndex
from wagtail.search import index as index
from wagtail.search.queryset import SearchableQuerySetMixin as SearchableQuerySetMixin
from wagtail.utils.file import hash_filelike as hash_filelike

class DocumentQuerySet(SearchableQuerySetMixin, models.QuerySet): ...

class AbstractDocument(CollectionMember, index.Indexed, models.Model):
    id: int
    title: models.CharField[str, str]
    file: models.FileField[str, str]
    created_at: models.DateTimeField[datetime, datetime]
    uploaded_by_user: models.ForeignKey[AbstractBaseUser | None, AbstractBaseUser | None]
    tags: TaggableManager
    file_size: models.PositiveBigIntegerField[int | None, int | None]
    file_hash: models.CharField[str, str]
    objects: DocumentQuerySet
    search_fields: list[index.BaseField | index.RelatedFields]
    def clean(self) -> None: ...
    def is_stored_locally(self) -> bool: ...
    @contextmanager
    def open_file(self) -> Generator[File]: ...
    def get_file_size(self) -> int | None: ...
    def get_file_hash(self) -> str: ...
    @property
    def filename(self) -> str: ...
    @property
    def file_extension(self) -> str: ...
    @property
    def url(self) -> str: ...
    def get_usage(self) -> ReferenceGroups: ...
    @property
    def usage_url(self) -> str: ...
    def is_editable_by_user(self, user: models.Model) -> bool: ...
    @property
    def content_type(self) -> str: ...
    @property
    def content_disposition(self) -> str: ...
    class Meta:
        abstract: bool
        verbose_name: str
        verbose_name_plural: str

class Document(AbstractDocument):
    admin_form_fields: tuple[str, ...]
    class Meta(AbstractDocument.Meta):
        permissions: list[tuple[str, str]]

document_served: Signal
