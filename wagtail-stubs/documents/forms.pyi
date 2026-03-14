from typing import Any

from django.forms import FileInput
from wagtail.admin.forms.collections import BaseCollectionMemberForm as BaseCollectionMemberForm, CollectionChoiceField as CollectionChoiceField, collection_member_permission_formset_factory as collection_member_permission_formset_factory
from wagtail.admin.forms.tags import validate_tag_length as validate_tag_length
from wagtail.admin.widgets import AdminTagWidget as AdminTagWidget
from wagtail.documents.models import Document as Document
from wagtail.documents.permissions import permission_policy as documents_permission_policy
from wagtail.models import Collection as Collection

def formfield_for_dbfield(db_field: Any, **kwargs: Any) -> Any: ...

class BaseDocumentForm(BaseCollectionMemberForm):
    permission_policy = documents_permission_policy
    original_file: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def save(self, commit: bool = True) -> Any: ...
    class Meta:
        widgets: dict[str, type[AdminTagWidget] | FileInput]
    def clean_tags(self) -> Any: ...

def get_document_base_form() -> type[BaseDocumentForm]: ...
def get_document_form(model: type) -> type[BaseDocumentForm]: ...
def get_document_multi_form(model: type) -> type[BaseDocumentForm]: ...

GroupDocumentPermissionFormSet: type
