from collections.abc import Iterable

from _typeshed import Incomplete
from wagtail.contrib.frontend_cache.utils import PurgeBatch as PurgeBatch
from wagtail.coreutils import BatchCreator as BatchCreator
from wagtail.coreutils import get_dummy_request as get_dummy_request
from wagtail.models.pages import Page as Page
from wagtail.models.sites import Site as Site

from .models import Redirect as Redirect

logger: Incomplete

class BatchRedirectCreator(BatchCreator):
    model = Redirect
    def pre_process(self) -> None: ...
    def post_process(self) -> None: ...

def autocreate_redirects_on_slug_change(instance_before: Page, instance: Page, **kwargs): ...
def autocreate_redirects_on_page_move(instance: Page, url_path_after: str, url_path_before: str, **kwargs) -> None: ...
def create_redirects(page: Page, page_old: Page, sites: Iterable[Site]) -> None: ...
