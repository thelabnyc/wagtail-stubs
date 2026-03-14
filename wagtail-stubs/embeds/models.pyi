from typing import Any

from django.db import models

EMBED_TYPES: tuple[tuple[str, str], ...]

class Embed(models.Model):
    url: models.TextField[str, str]
    max_width: models.SmallIntegerField[int | None, int | None]
    hash: models.CharField[str, str]
    type: models.CharField[str, str]
    html: models.TextField[str, str]
    title: models.TextField[str, str]
    author_name: models.TextField[str, str]
    provider_name: models.TextField[str, str]
    thumbnail_url: models.TextField[str, str]
    width: models.IntegerField[int | None, int | None]
    height: models.IntegerField[int | None, int | None]
    last_updated: models.DateTimeField[Any, Any]
    cache_until: models.DateTimeField[Any, Any]
    class Meta:
        verbose_name: str
        verbose_name_plural: str
    @property
    def ratio(self) -> float | None: ...
    @property
    def ratio_css(self) -> str | None: ...
    @property
    def is_responsive(self) -> bool: ...
