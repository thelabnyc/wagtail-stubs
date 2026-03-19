from typing import Any

from django import forms

class BooleanRadioSelect(forms.RadioSelect):
    def __init__(self, attrs: dict[str, Any] | None = None) -> None: ...
