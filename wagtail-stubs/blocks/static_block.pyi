from typing import Any

from django.forms.utils import _DataT, _FilesT

from .base import Block

__all__ = ["StaticBlock"]

class StaticBlock(Block):
    class Meta:
        admin_text: str | None
        default: None

    def get_admin_text(self) -> str: ...
    def value_from_datadict(
        self, data: _DataT, files: _FilesT, prefix: str
    ) -> None: ...
    def normalize(self, value: Any) -> None: ...
    def render_basic(
        self, value: Any, context: dict[str, Any] | None = ...
    ) -> str: ...
