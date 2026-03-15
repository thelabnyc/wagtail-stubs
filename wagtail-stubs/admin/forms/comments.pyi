from typing import Any

from django.forms import BooleanField
from modelcluster.forms import BaseChildFormSet
from wagtail.admin.forms.models import WagtailAdminModelForm
from wagtail.models.pages import Comment

class CommentReplyForm(WagtailAdminModelForm):
    class Meta:
        fields: tuple[str, ...]

    def clean(self) -> dict[str, Any]: ...

class CommentForm(WagtailAdminModelForm):
    resolved: BooleanField
    class Meta:
        formsets: dict[str, dict[str, Any]]

    def clean(self) -> dict[str, Any]: ...
    def save(self, commit: bool = ...) -> Comment: ...

class CommentFormSet(BaseChildFormSet):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
