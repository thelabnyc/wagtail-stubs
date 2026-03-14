from django import forms

class SearchForm(forms.Form):
    q: forms.CharField
    def __init__(self, *args: object, placeholder: str = ..., **kwargs: object) -> None: ...
