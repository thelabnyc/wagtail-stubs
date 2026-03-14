from _typeshed import Incomplete
from django.db import models

EMBED_TYPES: Incomplete

class Embed(models.Model):
    url: Incomplete
    max_width: Incomplete
    hash: Incomplete
    type: Incomplete
    html: Incomplete
    title: Incomplete
    author_name: Incomplete
    provider_name: Incomplete
    thumbnail_url: Incomplete
    width: Incomplete
    height: Incomplete
    last_updated: Incomplete
    cache_until: Incomplete
    class Meta:
        verbose_name: Incomplete
        verbose_name_plural: Incomplete
    @property
    def ratio(self): ...
    @property
    def ratio_css(self): ...
    @property
    def is_responsive(self): ...
