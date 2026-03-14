from typing import Any

from wagtail.search.backends.base import BaseSearchResults

class SearchableQuerySetMixin:
    def search(self, query: str | Any = ..., fields: list[str] | None = None, operator: str | None = None, order_by_relevance: bool = True, backend: str = "default") -> BaseSearchResults: ...
    def autocomplete(self, query: str | Any = ..., fields: list[str] | None = None, operator: str | None = None, order_by_relevance: bool = True, backend: str = "default") -> BaseSearchResults: ...
