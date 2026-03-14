from wagtail.search.backends.elasticsearch8 import (
    Elasticsearch8AutocompleteQueryCompiler,
    Elasticsearch8SearchBackend,
    Elasticsearch8SearchQueryCompiler,
)

class Elasticsearch9SearchQueryCompiler(Elasticsearch8SearchQueryCompiler): ...
class Elasticsearch9AutocompleteQueryCompiler(Elasticsearch8AutocompleteQueryCompiler): ...

class Elasticsearch9SearchBackend(Elasticsearch8SearchBackend):
    query_compiler_class: type[Elasticsearch9SearchQueryCompiler]
    autocomplete_query_compiler_class: type[Elasticsearch9AutocompleteQueryCompiler]

SearchBackend = Elasticsearch9SearchBackend
