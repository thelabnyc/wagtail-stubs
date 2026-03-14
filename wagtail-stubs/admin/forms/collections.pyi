from typing import Any

from django import forms
from django.contrib.auth.models import Group
from django.db.models import QuerySet

from wagtail.admin.forms.formsets import BaseFormSetMixin
from wagtail.admin.forms.view_restrictions import BaseViewRestrictionForm
from wagtail.models import Collection, CollectionViewRestriction

class CollectionViewRestrictionForm(BaseViewRestrictionForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    class Meta:
        model: type[CollectionViewRestriction]
        fields: tuple[str, ...]

class SelectWithDisabledOptions(forms.Select):
    disabled_values: tuple[Any, ...] | list[Any]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def create_option(self, name: str, value: Any, *args: Any, **kwargs: Any) -> dict[str, Any]: ...

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
    permission_policy: Any
    collections: QuerySet[Collection]
    def __init__(self, *args: Any, user: Any | None = ..., **kwargs: Any) -> None: ...
    def save(self, commit: bool = ...) -> Any: ...

class BaseGroupCollectionMemberPermissionFormSet(BaseFormSetMixin, forms.BaseFormSet):
    permission_types: list[tuple[str, str, str]]
    permission_queryset: QuerySet[Any]
    default_prefix: str
    template: str
    instance: Group
    def __init__(
        self,
        data: dict[str, Any] | None = ...,
        files: dict[str, Any] | None = ...,
        instance: Group | None = ...,
        prefix: str | None = ...,
    ) -> None: ...
    def clean(self) -> None: ...
    def save(self) -> None: ...
    def as_admin_panel(self) -> str: ...

def collection_member_permission_formset_factory(
    model: type[Any],
    permission_types: list[tuple[str, str, str]],
    template: str,
    default_prefix: str | None = ...,
) -> type[BaseGroupCollectionMemberPermissionFormSet]: ...

GroupCollectionManagementPermissionFormSet: type[BaseGroupCollectionMemberPermissionFormSet]
