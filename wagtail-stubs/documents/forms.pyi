from collections.abc import Iterable
from typing import Any

from django.core.files import File
from django.db import models
from django.forms import FileInput
from django.forms.fields import Field as FormField
from django.utils.functional import cached_property
from wagtail.admin.forms.collections import (
    BaseCollectionMemberForm as BaseCollectionMemberForm,
)
from wagtail.admin.forms.collections import (
    CollectionChoiceField as CollectionChoiceField,
)
from wagtail.admin.forms.collections import (
    collection_member_permission_formset_factory as collection_member_permission_formset_factory,
)
from wagtail.admin.forms.tags import validate_tag_length as validate_tag_length
from wagtail.admin.widgets import AdminTagWidget as AdminTagWidget
from wagtail.documents.models import AbstractDocument
from wagtail.documents.models import Document as Document
from wagtail.permission_policies.base import BasePermissionPolicy

def formfield_for_dbfield(db_field: models.Field[Any, Any], **kwargs: Any) -> FormField: ...

class BaseDocumentForm(BaseCollectionMemberForm):
    @cached_property
    def permission_policy(self) -> BasePermissionPolicy[AbstractDocument]: ...  # type: ignore[override]
    original_file: File
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def save(self, commit: bool = True) -> models.Model: ...
    class Meta:
        widgets: dict[str, type[AdminTagWidget] | FileInput]

    def clean_tags(self) -> list[str]: ...

def get_document_base_form() -> type[BaseDocumentForm]: ...
def get_document_form(model: type[AbstractDocument], fields: Iterable[str] | None = None) -> type[BaseDocumentForm]: ...
def get_document_multi_form(model: type) -> type[BaseDocumentForm]: ...

GroupDocumentPermissionFormSet: type
