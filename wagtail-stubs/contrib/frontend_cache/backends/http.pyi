from .base import BaseBackend
from _typeshed import Incomplete
from urllib.request import Request

__all__ = ['PurgeRequest', 'HTTPBackend']

class PurgeRequest(Request):
    def get_method(self): ...

class HTTPBackend(BaseBackend):
    cache_scheme: Incomplete
    cache_netloc: Incomplete
    def __init__(self, params) -> None: ...
    def purge(self, url) -> None: ...
