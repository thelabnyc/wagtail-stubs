from _typeshed import Incomplete
from django import forms

class PasswordViewRestrictionForm(forms.Form):
    password: Incomplete
    return_url: Incomplete
    restriction: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def clean_password(self): ...

class TaskStateCommentForm(forms.Form):
    comment: Incomplete
