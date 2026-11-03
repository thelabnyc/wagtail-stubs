from typing import ClassVar

from .base import BaseBackend as BaseBackend

class DummyBackend(BaseBackend):
    urls: ClassVar[list[str]]
    def purge(self, url: str) -> None: ...
    @classmethod
    def reset(cls) -> None: ...
