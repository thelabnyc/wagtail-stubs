from typing import Any

from wagtail.models.pages import AbstractPage

class RouteResult:
    page: AbstractPage
    args: list[Any]
    kwargs: dict[str, Any]
    def __init__(
        self, page: AbstractPage, args: list[Any] | None = None, kwargs: dict[str, Any] | None = None
    ) -> None: ...
    def __getitem__(self, index: int) -> Any: ...
