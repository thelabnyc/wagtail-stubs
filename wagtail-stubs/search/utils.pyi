from collections.abc import Callable, Iterator, Sequence
from functools import partial
from typing import Any
import re

from django.db.backends.base.base import BaseDatabaseWrapper
from django.http import QueryDict
from wagtail.search.index import BaseField, RelatedFields, SearchField
from wagtail.search.query import SearchQuery

MAX_QUERY_STRING_LENGTH: int
NOT_SET: object

OR: partial[Any]
AND: partial[Any]
ADD: partial[Any]
MUL: partial[Any]

filters_regexp: re.Pattern[str]

def normalise_query_string(query_string: str) -> str: ...
def parse_query_string(
    query_string: str,
    operator: str | None = None,
    zero_terms: SearchQuery = ...,
) -> tuple[QueryDict, SearchQuery]: ...
def separate_filters_from_query(query_string: str) -> tuple[QueryDict, str]: ...
def get_search_fields(search_fields: list[BaseField | RelatedFields]) -> Iterator[SearchField]: ...
def get_descendants_content_types_pks(model: type) -> list[int]: ...
def get_ancestors_content_types_pks(model: type) -> list[int]: ...
def get_content_type_pk(model: type) -> int: ...
def get_descendant_models(model: type) -> set[type]: ...
def balanced_reduce[T](operator: Callable[[T, T], T], seq: Sequence[T], initializer: T = ...) -> T: ...
def get_postgresql_connections() -> list[BaseDatabaseWrapper]: ...
