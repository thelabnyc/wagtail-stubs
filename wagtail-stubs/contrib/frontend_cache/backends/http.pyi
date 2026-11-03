from typing import Any
from urllib.request import Request

from .base import BaseBackend

__all__ = ["PurgeRequest", "HTTPBackend"]

class PurgeRequest(Request):
    def get_method(self) -> str: ...

class HTTPBackend(BaseBackend):
    cache_scheme: str
    cache_netloc: str
    def __init__(self, params: dict[str, Any]) -> None: ...
    def purge(self, url: str) -> None: ...
