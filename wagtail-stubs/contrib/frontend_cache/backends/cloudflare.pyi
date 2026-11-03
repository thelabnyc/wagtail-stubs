from collections.abc import Sequence
from typing import Any, ClassVar

from .base import BaseBackend

__all__ = ["CloudflareBackend"]

class CloudflareBackend(BaseBackend):
    CHUNK_SIZE: ClassVar[int]
    purge_batch_size: int
    cloudflare_email: str | None
    cloudflare_api_key: str | None
    cloudflare_token: str | None
    cloudflare_zoneid: str
    cloudflare_purge_endpoint_url: str
    def __init__(self, params: dict[str, Any]) -> None: ...
    def purge_batch(self, urls: Sequence[str]) -> None: ...
    def purge(self, url: str) -> None: ...
