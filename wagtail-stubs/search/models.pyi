from _typeshed import Incomplete
from modelsearch.abstract_models import AbstractIndexEntry, AbstractSQLiteFTSIndexEntry

class IndexEntry(AbstractIndexEntry):
    class Meta(AbstractIndexEntry.Meta):
        abstract: bool

class SQLiteFTSIndexEntry(AbstractSQLiteFTSIndexEntry):
    index_entry: Incomplete
    class Meta(AbstractSQLiteFTSIndexEntry.Meta):
        abstract: bool
        db_table: str
