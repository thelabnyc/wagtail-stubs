from collections.abc import Callable
from typing import Any

from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import Field, Model
from django.forms.fields import Field as FormField
from modelcluster.forms import (
    BaseChildFormSet,
    ClusterForm,
    ClusterFormMetaclass,
    ClusterFormOptions,
)
from permissionedforms import (
    PermissionedForm,
    PermissionedFormMetaclass,
    PermissionedFormOptionsMixin,
)
from wagtail.utils.registry import ModelFieldRegistry

registry: ModelFieldRegistry

FORM_FIELD_OVERRIDES: dict[type, dict[str, Any]]
DIRECT_FORM_FIELD_OVERRIDES: dict[type, dict[str, Any]]

def register_form_field_override(
    db_field_class: type[Field[Any, Any]],
    to: type[Model] | str | None = None,
    override: dict[str, Any] | None = None,
    exact_class: bool = False,
) -> None: ...
def formfield_for_dbfield(db_field: Field[Any, Any], **kwargs: Any) -> FormField | None: ...

class WagtailAdminModelFormOptions(PermissionedFormOptionsMixin, ClusterFormOptions):
    defer_required_on_fields: list[str]
    def __init__(self, options: type | None = None) -> None: ...

class WagtailAdminModelFormMetaclass(PermissionedFormMetaclass, ClusterFormMetaclass):  # type: ignore[misc]
    options_class: type[WagtailAdminModelFormOptions]  # type: ignore[assignment]
    extra_form_count: int
    @classmethod
    def child_form(cls) -> type[WagtailAdminModelForm]: ...

class WagtailAdminModelForm(
    PermissionedForm,
    ClusterForm,
    metaclass=WagtailAdminModelFormMetaclass,  # type: ignore[misc]
):
    for_user: AbstractBaseUser | None
    deferred_required_fields: list[str]
    deferred_formset_min_nums: dict[str, int]
    formsets: dict[str, BaseChildFormSet]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def defer_required_fields(self) -> None: ...
    def restore_required_fields(self) -> None: ...
    def get_field_updates_for_resave(self) -> list[tuple[str, Any]]: ...

    class Meta:
        formfield_callback: Callable[..., FormField | None]

class WagtailAdminDraftStateFormMixin:
    @property
    def show_schedule_publishing_toggle(self) -> bool: ...
    def clean(self) -> dict[str, Any]: ...
