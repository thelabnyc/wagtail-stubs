from typing import Any

from .base import Block

__all__ = ["StaticBlock"]

class StaticBlock(Block):
    class Meta:
        admin_text: str | None
        default: None

    def get_admin_text(self) -> str: ...
    def value_from_datadict(
        self, data: Any, files: Any, prefix: str
    ) -> None: ...
    def normalize(self, value: Any) -> None: ...
    def render_basic(
        self, value: Any, context: dict[str, Any] | None = ...
    ) -> str: ...
