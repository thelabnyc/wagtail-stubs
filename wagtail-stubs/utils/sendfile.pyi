from collections.abc import Callable
from typing import Any, Literal

from django.http import HttpRequest, HttpResponse

VERSION: tuple[int, int, int]
__version__: str

def sendfile(request: HttpRequest, filename: str, attachment: bool = False, attachment_filename: str | Literal[False] | None = None, mimetype: str | None = None, encoding: str | None = None, backend: Callable[..., HttpResponse] | None = None) -> HttpResponse: ...
