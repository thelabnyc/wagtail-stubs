from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager
from django.db import models
from wagtail.models import CollectionMember as CollectionMember, ReferenceIndex as ReferenceIndex
from wagtail.search import index as index
from wagtail.search.queryset import SearchableQuerySetMixin as SearchableQuerySetMixin
from wagtail.utils.file import hash_filelike as hash_filelike

class DocumentQuerySet(SearchableQuerySetMixin, models.QuerySet): ...

class AbstractDocument(CollectionMember, index.Indexed, models.Model):
    title: Incomplete
    file: Incomplete
    created_at: Incomplete
    uploaded_by_user: Incomplete
    tags: Incomplete
    file_size: Incomplete
    file_hash: Incomplete
    objects: Incomplete
    search_fields: Incomplete
    def clean(self) -> None: ...
    def is_stored_locally(self): ...
    @contextmanager
    def open_file(self) -> Generator[Incomplete]: ...
    def get_file_size(self): ...
    def get_file_hash(self): ...
    @property
    def filename(self): ...
    @property
    def file_extension(self): ...
    @property
    def url(self): ...
    def get_usage(self): ...
    @property
    def usage_url(self): ...
    def is_editable_by_user(self, user): ...
    @property
    def content_type(self): ...
    @property
    def content_disposition(self): ...
    class Meta:
        abstract: bool
        verbose_name: Incomplete
        verbose_name_plural: Incomplete

class Document(AbstractDocument):
    admin_form_fields: Incomplete
    class Meta(AbstractDocument.Meta):
        permissions: Incomplete

document_served: Incomplete
