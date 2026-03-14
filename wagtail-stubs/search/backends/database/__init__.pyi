from typing import Any

from wagtail.search.backends.base import BaseSearchBackend

def SearchBackend(params: dict[str, Any]) -> BaseSearchBackend: ...
