from _typeshed import Incomplete
from wagtail.coreutils import get_content_languages as get_content_languages

from .utils import get_backends as get_backends

logger: Incomplete

def purge_urls_from_cache_task(urls, backend_settings=None, backends=None) -> None: ...
