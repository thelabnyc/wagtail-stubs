from collections import OrderedDict
from functools import partial
from typing import Any

from django.db import models
from django.db.models import Q, QuerySet
from wagtail.search.backends.base import BaseSearchBackend, BaseSearchQueryCompiler, BaseSearchResults
from wagtail.search.query import SearchQuery

class DatabaseSearchQueryCompiler(BaseSearchQueryCompiler):
    DEFAULT_OPERATOR: str
    HANDLES_ORDER_BY_EXPRESSIONS: bool
    OPERATORS: dict[str, partial[Any]]
    fields_names: list[str]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_fields_names(self) -> list[str]: ...
    def build_single_term_filter(self, term: str) -> Q: ...
    def check_boost(self, query: SearchQuery, boost: float = ...) -> None: ...
    def build_database_filter(self, query: SearchQuery, boost: float = ...) -> Q | str: ...

class DatabaseAutocompleteQueryCompiler(DatabaseSearchQueryCompiler): ...

class DatabaseSearchResults(BaseSearchResults):
    iterator_chunk_size: int
    supports_facet: bool
    def get_queryset(self) -> QuerySet[models.Model]: ...
    def facet(self, field_name: str) -> OrderedDict[str, int]: ...

class DatabaseSearchBackend(BaseSearchBackend):
    query_compiler_class: type[DatabaseSearchQueryCompiler]
    autocomplete_query_compiler_class: type[DatabaseSearchQueryCompiler]
    results_class: type[DatabaseSearchResults]

SearchBackend = DatabaseSearchBackend
