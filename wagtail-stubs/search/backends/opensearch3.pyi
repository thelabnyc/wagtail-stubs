from wagtail.search.backends.elasticsearch8 import (
    Elasticsearch8AutocompleteQueryCompiler,
    Elasticsearch8SearchBackend,
    Elasticsearch8SearchQueryCompiler,
)

class OpenSearch3SearchQueryCompiler(Elasticsearch8SearchQueryCompiler): ...
class OpenSearch3AutocompleteQueryCompiler(Elasticsearch8AutocompleteQueryCompiler): ...

class OpenSearch3SearchBackend(Elasticsearch8SearchBackend):
    query_compiler_class: type[OpenSearch3SearchQueryCompiler]
    autocomplete_query_compiler_class: type[OpenSearch3AutocompleteQueryCompiler]

SearchBackend = OpenSearch3SearchBackend
