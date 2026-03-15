from collections.abc import Callable, Sequence
from typing import Any

from django.urls import URLPattern, URLResolver

def decorate_urlpatterns(
    urlpatterns: Sequence[URLPattern | URLResolver], decorator: Callable[..., Any]
) -> Sequence[URLPattern | URLResolver]: ...
