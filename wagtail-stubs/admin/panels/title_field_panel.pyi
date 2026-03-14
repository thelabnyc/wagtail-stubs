from typing import Any

from .field_panel import FieldPanel

class TitleFieldPanel(FieldPanel):
    apply_if_live: bool
    placeholder: bool | str
    targets: list[str]

    def __init__(
        self,
        *args: Any,
        apply_if_live: bool = False,
        classname: str = "title",
        placeholder: bool | str = True,
        targets: list[str] = ...,
        **kwargs: Any,
    ) -> None: ...
    def clone_kwargs(self) -> dict[str, Any]: ...

    class BoundPanel(FieldPanel.BoundPanel):
        apply_actions: list[str]

        def get_context_data(self, parent_context: dict[str, Any] | None = None) -> dict[str, Any]: ...
        def get_attrs(self) -> dict[str, str]: ...
        def get_placeholder(self) -> str | None: ...
        def get_should_apply(self) -> bool: ...
        def get_target_selector(self, target: str) -> str: ...
