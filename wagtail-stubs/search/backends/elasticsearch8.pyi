from django.db import models

from wagtail.search.backends.elasticsearch7 import (
    Elasticsearch7AutocompleteQueryCompiler,
    Elasticsearch7Index,
    Elasticsearch7Mapping,
    Elasticsearch7SearchBackend,
    Elasticsearch7SearchQueryCompiler,
    Elasticsearch7SearchResults,
)

class Elasticsearch8Mapping(Elasticsearch7Mapping): ...

class Elasticsearch8Index(Elasticsearch7Index):
    def put(self) -> None: ...
    def delete(self) -> None: ...
    def refresh(self) -> None: ...
    def add_model(self, model: type) -> None: ...
    def add_item(self, item: models.Model) -> None: ...

class Elasticsearch8SearchQueryCompiler(Elasticsearch7SearchQueryCompiler):
    mapping_class: type[Elasticsearch8Mapping]

class Elasticsearch8SearchResults(Elasticsearch7SearchResults): ...

class Elasticsearch8AutocompleteQueryCompiler(Elasticsearch7AutocompleteQueryCompiler):
    mapping_class: type[Elasticsearch8Mapping]

class Elasticsearch8SearchBackend(Elasticsearch7SearchBackend):
    mapping_class: type[Elasticsearch8Mapping]
    index_class: type[Elasticsearch8Index]
    query_compiler_class: type[Elasticsearch8SearchQueryCompiler]
    autocomplete_query_compiler_class: type[Elasticsearch8AutocompleteQueryCompiler]
    results_class: type[Elasticsearch8SearchResults]

SearchBackend = Elasticsearch8SearchBackend
