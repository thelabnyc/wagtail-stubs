from typing import Any

from django import forms
from django.contrib.auth.models import AbstractBaseUser
from wagtail.admin.forms.models import WagtailAdminModelForm
from wagtail.admin.forms.view_restrictions import BaseViewRestrictionForm
from wagtail.models.pages import Page, PageSubscription, PageViewRestriction

class CopyForm(forms.Form):
    page: Page
    user: AbstractBaseUser | None
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def clean(self) -> dict[str, Any]: ...

class PageViewRestrictionForm(BaseViewRestrictionForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    class Meta:
        model: type[PageViewRestriction]
        fields: tuple[str, ...]

class WagtailAdminPageForm(WagtailAdminModelForm):
    comment_notifications: forms.BooleanField
    subscription: PageSubscription | None
    parent_page: Page | None
    def __init__(
        self,
        data: dict[str, Any] | None = ...,
        files: dict[str, Any] | None = ...,
        parent_page: Page | None = ...,
        subscription: PageSubscription | None = ...,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def serialize_comments(self, user: AbstractBaseUser) -> dict[str, Any]: ...
    @property
    def show_comments_toggle(self) -> bool: ...
    def save(self, commit: bool = ...) -> Page: ...
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
    user: AbstractBaseUser
    def __init__(self, child_page_type: type[Page], user: AbstractBaseUser, *args: Any, **kwargs: Any) -> None: ...
    def clean_parent_page(self) -> Page: ...
