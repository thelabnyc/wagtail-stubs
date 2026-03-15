from _typeshed import Incomplete
from django.db import models
from wagtail.search.utils import (
    MAX_QUERY_STRING_LENGTH as MAX_QUERY_STRING_LENGTH,
)
from wagtail.search.utils import (
    normalise_query_string as normalise_query_string,
)

class Query(models.Model):
    query_string: Incomplete
    def save(self, *args, **kwargs) -> None: ...
    def add_hit(self, date=None) -> None: ...
    @property
    def hits(self): ...
    @classmethod
    def garbage_collect(cls) -> None: ...
    @classmethod
    def get(cls, query_string): ...
    @classmethod
    def get_most_popular(cls, date_since=None): ...

class QueryDailyHits(models.Model):
    query: Incomplete
    date: Incomplete
    hits: Incomplete
    @classmethod
    def garbage_collect(cls, days=None) -> None: ...
    class Meta:
        unique_together: Incomplete
        verbose_name: Incomplete
        verbose_name_plural: Incomplete

class SearchPromotion(models.Model):
    query: Incomplete
    page: Incomplete
    external_link_url: Incomplete
    external_link_text: Incomplete
    description: Incomplete
    sort_order: Incomplete
    @property
    def title(self): ...
    @property
    def link(self) -> str: ...
    class Meta:
        ordering: Incomplete
        verbose_name: Incomplete
