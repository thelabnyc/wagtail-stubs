from typing import Any

from wagtail.models import Page

class RouteResult:
    page: Page
    args: list[Any]
    kwargs: dict[str, Any]
    def __init__(self, page: Page, args: list[Any] | None = None, kwargs: dict[str, Any] | None = None) -> None: ...
    def __getitem__(self, index: int) -> Any: ...
