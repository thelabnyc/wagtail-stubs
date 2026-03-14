from typing import Any

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

class TextIDGenericRelation(GenericRelation):
    auto_created: bool

class BaseIndexEntry(models.Model):
    content_type: models.ForeignKey[ContentType, ContentType]
    object_id: models.CharField[str, str]
    content_object: GenericForeignKey
    title_norm: models.FloatField[float, float]
    wagtail_reference_index_ignore: bool
    @property
    def model(self) -> str: ...
    @classmethod
    def add_generic_relations(cls) -> None: ...
    class Meta:
        unique_together: list[tuple[str, str]]
        verbose_name: str
        verbose_name_plural: str
        abstract: bool

class IndexEntry(BaseIndexEntry):
    class Meta(BaseIndexEntry.Meta):
        abstract: bool
