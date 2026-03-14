from .base import BaseBackend as BaseBackend
from _typeshed import Incomplete

class DummyBackend(BaseBackend):
    urls: Incomplete
    def __init__(self) -> None: ...
    def purge(self, url) -> None: ...
