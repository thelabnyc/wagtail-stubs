from .base import BaseBackend
from _typeshed import Incomplete

__all__ = ['CloudflareBackend']

class CloudflareBackend(BaseBackend):
    CHUNK_SIZE: int
    cloudflare_email: Incomplete
    cloudflare_api_key: Incomplete
    cloudflare_token: Incomplete
    cloudflare_zoneid: Incomplete
    cloudflare_purge_endpoint_url: Incomplete
    def __init__(self, params) -> None: ...
    def purge_batch(self, urls) -> None: ...
    def purge(self, url) -> None: ...
