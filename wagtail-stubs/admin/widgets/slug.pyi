from typing import Any
import re

from django.forms import widgets

class SlugInput(widgets.TextInput):
    def __init__(
        self,
        attrs: dict[str, Any] | None = None,
        formatters: list[tuple[re.Pattern[str] | str | bytes, str | None]] | None = None,
        locale: object | None = None,
    ) -> None: ...
