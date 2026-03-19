from typing import Any

from django import forms
from django.contrib.auth.models import Group
from django.db.models.query import QuerySet
from wagtail.models.view_restrictions import BaseViewRestriction

class BaseViewRestrictionForm(forms.ModelForm[BaseViewRestriction]):
    restriction_type: forms.ChoiceField
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def clean_password(self) -> str: ...
    def clean_groups(self) -> QuerySet[Group]: ...

    class Meta:
        model: type[BaseViewRestriction]
        fields: tuple[str, ...]
