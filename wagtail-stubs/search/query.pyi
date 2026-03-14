class SearchQuery:
    def __and__(self, other: SearchQuery) -> And: ...
    def __or__(self, other: SearchQuery) -> Or: ...
    def __invert__(self) -> Not: ...

class PlainText(SearchQuery):
    OPERATORS: list[str]
    DEFAULT_OPERATOR: str
    query_string: str
    operator: str
    boost: float
    def __init__(self, query_string: str, operator: str = ..., boost: float = 1.0) -> None: ...

class Phrase(SearchQuery):
    query_string: str
    def __init__(self, query_string: str) -> None: ...

class Fuzzy(SearchQuery):
    OPERATORS: list[str]
    DEFAULT_OPERATOR: str
    query_string: str
    operator: str
    def __init__(self, query_string: str, operator: str = ...) -> None: ...

class Boost(SearchQuery):
    subquery: SearchQuery
    boost: float
    def __init__(self, subquery: SearchQuery, boost: float) -> None: ...

class And(SearchQuery):
    subqueries: list[SearchQuery]
    def __init__(self, subqueries: list[SearchQuery]) -> None: ...

class Or(SearchQuery):
    subqueries: list[SearchQuery]
    def __init__(self, subqueries: list[SearchQuery]) -> None: ...

class Not(SearchQuery):
    subquery: SearchQuery
    def __init__(self, subquery: SearchQuery) -> None: ...

class MatchAll(SearchQuery): ...

MATCH_ALL: MatchAll
MATCH_NONE: Not
