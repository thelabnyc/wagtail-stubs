from http import HTTPMethod as HTTPMethod
from typing import Any

from django import forms

AUTH_USER_MODEL: str
AUTH_USER_APP_LABEL: str
AUTH_USER_MODEL_NAME: str

class URLField(forms.URLField):
    def __init__(self, *, assume_scheme: str | None = None, **kwargs: Any) -> None: ...
