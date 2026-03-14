from wagtail.search.backends.elasticsearch7 import (
    Elasticsearch7AutocompleteQueryCompiler,
    Elasticsearch7SearchBackend,
    Elasticsearch7SearchQueryCompiler,
)

class OpenSearch2SearchQueryCompiler(Elasticsearch7SearchQueryCompiler): ...
class OpenSearch2AutocompleteQueryCompiler(Elasticsearch7AutocompleteQueryCompiler): ...

class OpenSearch2SearchBackend(Elasticsearch7SearchBackend):
    query_compiler_class: type[OpenSearch2SearchQueryCompiler]
    autocomplete_query_compiler_class: type[OpenSearch2AutocompleteQueryCompiler]

SearchBackend = OpenSearch2SearchBackend
