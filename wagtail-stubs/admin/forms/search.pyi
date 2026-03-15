from typing import Any

from django import forms

class SearchForm(forms.Form):
    q: forms.CharField
    def __init__(self, *args: Any, placeholder: str = ..., **kwargs: Any) -> None: ...
