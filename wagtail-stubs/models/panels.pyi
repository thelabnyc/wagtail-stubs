from typing import Any

class PanelPlaceholder:
    def __init__(self, class_path: str, args: list[Any], kwargs: dict[str, Any]) -> None: ...

class CommentPanelPlaceholder:
    def __init__(self) -> None: ...
