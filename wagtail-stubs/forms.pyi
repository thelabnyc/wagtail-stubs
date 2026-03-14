from django import forms

class PasswordViewRestrictionForm(forms.Form):
    password: forms.CharField
    return_url: forms.CharField
    restriction: object
    def __init__(self, *args: object, **kwargs: object) -> None: ...
    def clean_password(self) -> str: ...

class TaskStateCommentForm(forms.Form):
    comment: forms.CharField
