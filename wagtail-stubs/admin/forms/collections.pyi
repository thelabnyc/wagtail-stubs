from collections.abc import Mapping
from typing import Any

from django import forms
from django.contrib.auth.models import AbstractBaseUser, Group, Permission
from django.core.files.uploadedfile import UploadedFile
from django.db.models import Model, QuerySet
from django.utils.datastructures import MultiValueDict

from wagtail.admin.forms.formsets import BaseFormSetMixin
from wagtail.admin.forms.view_restrictions import BaseViewRestrictionForm
from wagtail.models import Collection, CollectionViewRestriction
from wagtail.permission_policies.base import BasePermissionPolicy

class CollectionViewRestrictionForm(BaseViewRestrictionForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    class Meta:
        model: type[CollectionViewRestriction]
        fields: tuple[str, ...]

class SelectWithDisabledOptions(forms.Select):
    disabled_values: tuple[str | int, ...] | list[str | int]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def create_option(
        self,
        name: str,
        value: Any,
        label: int | str,
        selected: bool,
        index: int,
        subindex: int | None = ...,
        attrs: dict[str, Any] | None = ...,
    ) -> dict[str, Any]: ...

class CollectionChoiceField(forms.ModelChoiceField):
    widget: type[SelectWithDisabledOptions]
    disabled_queryset: QuerySet[Collection] | None
    def __init__(self, *args: Any, disabled_queryset: QuerySet[Collection] | None = ..., **kwargs: Any) -> None: ...
    def label_from_instance(self, obj: Collection) -> str: ...

class CollectionForm(forms.ModelForm):
    parent: CollectionChoiceField
    class Meta:
        model: type[Collection]
        fields: tuple[str, ...]
    def clean_parent(self) -> Collection: ...

class BaseCollectionMemberForm(forms.ModelForm):
    permission_policy: BasePermissionPolicy
    collections: QuerySet[Collection]
    def __init__(self, *args: Any, user: AbstractBaseUser | None = ..., **kwargs: Any) -> None: ...
    def save(self, commit: bool = ...) -> Model: ...

class BaseGroupCollectionMemberPermissionFormSet(BaseFormSetMixin, forms.BaseFormSet):
    permission_types: list[tuple[str, str, str]]
    permission_queryset: QuerySet[Permission]
    default_prefix: str
    template: str
    instance: Group
    def __init__(
        self,
        data: Mapping[str, Any] | None = ...,
        files: MultiValueDict[str, UploadedFile] | None = ...,
        instance: Group | None = ...,
        prefix: str | None = ...,
    ) -> None: ...
    def clean(self) -> None: ...
    def save(self) -> None: ...
    def as_admin_panel(self) -> str: ...

def collection_member_permission_formset_factory(
    model: type[Model],
    permission_types: list[tuple[str, str, str]],
    template: str,
    default_prefix: str | None = ...,
) -> type[BaseGroupCollectionMemberPermissionFormSet]: ...

GroupCollectionManagementPermissionFormSet: type[BaseGroupCollectionMemberPermissionFormSet]
