from _typeshed import Incomplete

from .base import BaseBackend as BaseBackend

class DummyBackend(BaseBackend):
    urls: Incomplete
    def __init__(self) -> None: ...
    def purge(self, url) -> None: ...
