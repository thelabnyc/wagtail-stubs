from collections.abc import Iterable
from typing import Any

from _typeshed import Incomplete
from wagtail.contrib.frontend_cache.utils import PurgeBatch as PurgeBatch
from wagtail.coreutils import BatchCreator as BatchCreator
from wagtail.coreutils import get_dummy_request as get_dummy_request
from wagtail.models import AbstractPage
from wagtail.models.sites import Site as Site

from .models import Redirect as Redirect

Page: type[AbstractPage]

logger: Incomplete

class BatchRedirectCreator(BatchCreator):
    model = Redirect
    def pre_process(self) -> None: ...
    def post_process(self) -> None: ...

def should_autocreate_redirects(page: AbstractPage) -> bool: ...
def autocreate_redirects_on_slug_change(
    instance_before: AbstractPage, instance: AbstractPage, **kwargs: Any
) -> None: ...
def autocreate_redirects_on_page_move(
    instance: AbstractPage, url_path_after: str, url_path_before: str, **kwargs: Any
) -> None: ...
def create_redirects(page: AbstractPage, page_old: AbstractPage, sites: Iterable[Site]) -> None: ...
