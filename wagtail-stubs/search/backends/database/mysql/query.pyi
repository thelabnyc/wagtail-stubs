from typing import Any

from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.models import Field
from django.db.models.expressions import CombinedExpression, Expression, Value
from django.db.models.sql.compiler import SQLCompiler

class SearchQueryField(Field[Any, Any]):
    def db_type(self, connection: BaseDatabaseWrapper) -> None: ...

class LexemeCombinable(Expression):
    BITAND: str
    BITOR: str
    invert: bool
    def bitand(self, other: LexemeCombinable) -> CombinedLexeme: ...
    def bitor(self, other: LexemeCombinable) -> CombinedLexeme: ...
    def __or__(self, other: LexemeCombinable) -> CombinedLexeme: ...
    def __and__(self, other: LexemeCombinable) -> CombinedLexeme: ...

class Lexeme(LexemeCombinable, Value):
    def __init__(
        self,
        value: str,
        output_field: Field[Any, Any] | None = None,
        invert: bool = False,
        prefix: bool = False,
        weight: str | None = None,
    ) -> None: ...
    def as_sql(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper) -> tuple[str, list[str]]: ...

class CombinedLexeme(LexemeCombinable):
    def __init__(
        self, lhs: LexemeCombinable, connector: str, rhs: LexemeCombinable, output_field: Field[Any, Any] | None = None
    ) -> None: ...
    def as_sql(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper) -> tuple[str, list[str]]: ...

class SearchQueryCombinable:
    BITAND: str
    BITOR: str
    def __or__(self, other: SearchQueryCombinable) -> CombinedSearchQuery: ...
    def __ror__(self, other: SearchQueryCombinable) -> CombinedSearchQuery: ...
    def __and__(self, other: SearchQueryCombinable) -> CombinedSearchQuery: ...
    def __rand__(self, other: SearchQueryCombinable) -> CombinedSearchQuery: ...

class SearchQuery(SearchQueryCombinable, Expression):
    def __init__(self, value: LexemeCombinable | str, search_type: str = "lexeme", **extra: Any) -> None: ...
    def as_sql(
        self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any
    ) -> tuple[str, list[Any]]: ...

class CombinedSearchQuery(SearchQueryCombinable, CombinedExpression):
    def __init__(
        self,
        lhs: SearchQueryCombinable,
        connector: str,
        rhs: SearchQueryCombinable,
        output_field: Field[Any, Any] | None = None,
    ) -> None: ...
    def as_sql(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper) -> tuple[str, list[str]]: ...

class MatchExpression(Expression):
    filterable: bool
    template: str
    def __init__(
        self, query: SearchQueryCombinable, columns: list[str] | None = None, output_field: Field[Any, Any] | None = ...
    ) -> None: ...
    def as_sql(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper) -> tuple[str, list[str]]: ...
