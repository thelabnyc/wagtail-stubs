from collections import OrderedDict
from typing import Any

from django.db.models import QuerySet

from wagtail.search.backends.base import BaseSearchBackend, BaseSearchQueryCompiler, BaseSearchResults

class DatabaseSearchQueryCompiler(BaseSearchQueryCompiler):
    DEFAULT_OPERATOR: str
    OPERATORS: dict[str, str]
    fields_names: list[str]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_fields_names(self) -> list[str]: ...
    def build_single_term_filter(self, term: str) -> Any: ...
    def check_boost(self, query: Any, boost: float = ...) -> None: ...
    def build_database_filter(self, query: Any, boost: float = ...) -> Any: ...

class DatabaseAutocompleteQueryCompiler(DatabaseSearchQueryCompiler): ...

class DatabaseSearchResults(BaseSearchResults):
    iterator_chunk_size: int
    supports_facet: bool
    def get_queryset(self) -> QuerySet[Any]: ...
    def facet(self, field_name: str) -> OrderedDict[Any, int]: ...

class DatabaseSearchBackend(BaseSearchBackend):
    query_compiler_class: type[DatabaseSearchQueryCompiler]
    autocomplete_query_compiler_class: type[DatabaseSearchQueryCompiler]
    results_class: type[DatabaseSearchResults]

SearchBackend = DatabaseSearchBackend
