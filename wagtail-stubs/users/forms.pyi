from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import Group, Permission
from django.db import transaction
from django.db.models import QuerySet
from wagtail import hooks as hooks
from wagtail.admin.forms.formsets import BaseFormSetMixin as BaseFormSetMixin
from wagtail.admin.widgets import AdminPageChooser as AdminPageChooser
from wagtail.models.pages import PAGE_PERMISSION_CODENAMES as PAGE_PERMISSION_CODENAMES
from wagtail.models.pages import PAGE_PERMISSION_TYPES as PAGE_PERMISSION_TYPES
from wagtail.models.pages import GroupPagePermission as GroupPagePermission
from wagtail.models.pages import Page as Page

User: type[AbstractBaseUser]
standard_fields: set[str]

class UsernameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def username_field(self): ...
    def separate_username_field(self): ...

class UserForm(UsernameForm):
    required_css_class: str
    @property
    def password_required(self): ...
    @property
    def password_enabled(self): ...
    error_messages: dict[str, str]
    email: forms.EmailField
    first_name: forms.CharField
    last_name: forms.CharField
    password1: forms.CharField
    password2: forms.CharField
    is_superuser: forms.BooleanField
    def __init__(self, *args, **kwargs) -> None: ...
    def clean_password2(self): ...
    def validate_password(self) -> None: ...
    def save(self, commit: bool = True): ...

class UserCreationForm(UserForm):
    class Meta:
        model = User
        fields: set[str]
        widgets: dict[str, type[forms.Widget]]

class UserEditForm(UserForm):
    password_required: bool
    def __init__(self, *args, **kwargs) -> None: ...
    class Meta:
        model = User
        fields: set[str]
        widgets: dict[str, type[forms.Widget]]

class GroupForm(forms.ModelForm):
    registered_permissions: QuerySet[Permission]
    def __init__(self, *args, **kwargs) -> None: ...
    required_css_class: str
    error_messages: dict[str, str]
    is_superuser: forms.BooleanField
    class Meta:
        model = Group
        fields: tuple[str, ...]
        widgets: dict[str, forms.Widget]

    def clean_name(self): ...
    def save(self, commit: bool = True): ...

class PagePermissionsForm(forms.Form):
    page: forms.ModelChoiceField
    permissions: forms.ModelMultipleChoiceField

class BaseGroupPagePermissionFormSet(BaseFormSetMixin, forms.BaseFormSet):
    permission_types = PAGE_PERMISSION_TYPES
    instance: Group
    def __init__(self, data=None, files=None, instance=None, prefix: str = "page_permissions") -> None: ...
    def clean(self) -> None: ...
    @transaction.atomic
    def save(self) -> None: ...
    def as_admin_panel(self): ...

GroupPagePermissionFormSet: type[BaseGroupPagePermissionFormSet]
