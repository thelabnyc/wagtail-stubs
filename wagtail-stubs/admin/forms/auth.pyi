from collections.abc import Generator

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm as DjangoPasswordChangeForm
from django.contrib.auth.forms import PasswordResetForm as DjangoPasswordResetForm
from django.http import HttpRequest

class LoginForm(AuthenticationForm):
    username: forms.CharField
    password: forms.CharField
    remember: forms.BooleanField
    error_messages: dict[str, str]
    def __init__(self, request: HttpRequest | None = ..., *args: Any, **kwargs: Any) -> None: ...
    @property
    def extra_fields(self) -> Generator[tuple[str, forms.BoundField], None, None]: ...
    def get_invalid_login_error(self) -> forms.ValidationError: ...

class PasswordResetForm(DjangoPasswordResetForm):
    email: forms.EmailField
    @property
    def extra_fields(self) -> Generator[tuple[str, forms.BoundField], None, None]: ...

class PasswordChangeForm(DjangoPasswordChangeForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
