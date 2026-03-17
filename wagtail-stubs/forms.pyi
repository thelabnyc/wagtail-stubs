from typing import Any

from django import forms
from wagtail.models.view_restrictions import BaseViewRestriction

class PasswordViewRestrictionForm(forms.Form):
    password: forms.CharField
    return_url: forms.CharField
    restriction: BaseViewRestriction
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def clean_password(self) -> str: ...

class TaskStateCommentForm(forms.Form):
    comment: forms.CharField
