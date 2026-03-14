from typing import Any

from django.utils.functional import cached_property

class PanelPlaceholder:
    path: str
    args: list[Any]
    kwargs: dict[str, Any]

    def __init__(self, path: str, args: list[Any], kwargs: dict[str, Any]) -> None: ...

    @cached_property
    def panel_class(self) -> type[Any]: ...

    def construct(self) -> Any: ...

class CommentPanelPlaceholder(PanelPlaceholder):
    def __init__(self) -> None: ...
    def construct(self) -> Any | None: ...
