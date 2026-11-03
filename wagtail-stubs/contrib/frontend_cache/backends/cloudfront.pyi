from collections.abc import Sequence
from typing import Any

from _typeshed import Incomplete

from .base import BaseBackend

__all__ = ["CloudfrontBackend"]

class CloudfrontBackend(BaseBackend):
    client: Incomplete
    cloudfront_distribution_id: str
    def __init__(self, params: dict[str, Any]) -> None: ...
    def purge_batch(self, urls: Sequence[str]) -> None: ...
    def purge(self, url: str) -> None: ...
