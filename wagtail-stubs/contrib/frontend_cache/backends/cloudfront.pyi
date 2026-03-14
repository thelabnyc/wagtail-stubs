from .base import BaseBackend
from _typeshed import Incomplete

__all__ = ['CloudfrontBackend']

class CloudfrontBackend(BaseBackend):
    client: Incomplete
    cloudfront_distribution_id: Incomplete
    def __init__(self, params) -> None: ...
    def purge_batch(self, urls) -> None: ...
    def purge(self, url) -> None: ...
