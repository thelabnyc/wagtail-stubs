from typing import Any

from django import forms

from wagtail.admin.forms.models import WagtailAdminModelForm
from wagtail.admin.forms.view_restrictions import BaseViewRestrictionForm
from wagtail.models import Page, PageViewRestriction

class CopyForm(forms.Form):
    page: Page
    user: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def clean(self) -> dict[str, Any]: ...

class PageViewRestrictionForm(BaseViewRestrictionForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    class Meta:
        model: type[PageViewRestriction]
        fields: tuple[str, ...]

class WagtailAdminPageForm(WagtailAdminModelForm):
    comment_notifications: forms.BooleanField
    subscription: Any
    parent_page: Page | None
    def __init__(
        self,
        data: dict[str, Any] | None = ...,
        files: dict[str, Any] | None = ...,
        parent_page: Page | None = ...,
        subscription: Any | None = ...,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    @property
    def show_comments_toggle(self) -> bool: ...
    def save(self, commit: bool = ...) -> Any: ...
    def is_valid(self) -> bool: ...
    def clean(self) -> dict[str, Any]: ...
    @property
    def media(self) -> forms.Media: ...

class MoveForm(forms.Form):
    page_to_move: Page
    target_parent_models: list[type[Page]]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class ParentChooserForm(forms.Form):
    child_page_type: type[Page]
    user: Any
    def __init__(
        self, child_page_type: type[Page], user: Any, *args: Any, **kwargs: Any
    ) -> None: ...
    def clean_parent_page(self) -> Page: ...
