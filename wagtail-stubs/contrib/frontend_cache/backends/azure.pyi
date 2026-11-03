from collections.abc import Sequence
from typing import Any

from .base import BaseBackend

__all__ = ["AzureBaseBackend", "AzureFrontDoorBackend", "AzureCdnBackend"]

class AzureBaseBackend(BaseBackend):
    def __init__(self, params: dict[str, Any]) -> None: ...
    def purge_batch(self, urls: Sequence[str]) -> None: ...
    def purge(self, url: str) -> None: ...

class AzureFrontDoorBackend(AzureBaseBackend):
    def __init__(self, params: dict[str, Any]) -> None: ...

class AzureCdnBackend(AzureBaseBackend):
    def __init__(self, params: dict[str, Any]) -> None: ...
