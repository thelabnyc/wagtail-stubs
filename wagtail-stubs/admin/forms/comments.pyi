from typing import Any

from django.contrib.auth.models import AbstractBaseUser
from django.forms import BooleanField
from modelcluster.forms import BaseChildFormSet
from wagtail.admin.forms.models import WagtailAdminModelForm
from wagtail.models.pages import Comment

class CommentReplyForm(WagtailAdminModelForm):
    class Meta:
        fields: tuple[str, ...]

    def clean(self) -> dict[str, Any]: ...
    def serialize(self, bound: bool) -> tuple[dict[str, Any], set[int]]: ...

class CommentForm(WagtailAdminModelForm):
    resolved: BooleanField
    class Meta:
        formsets: dict[str, dict[str, Any]]

    def clean(self) -> dict[str, Any]: ...
    def save(self, commit: bool = ...) -> Comment: ...
    def serialize(self, bound: bool) -> tuple[dict[str, Any], set[int]]: ...

class CommentFormSet(BaseChildFormSet):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def serialize(self, bound: bool, user: AbstractBaseUser) -> dict[str, Any]: ...
