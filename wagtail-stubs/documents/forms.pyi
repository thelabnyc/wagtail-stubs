from _typeshed import Incomplete
from wagtail.admin.forms.collections import BaseCollectionMemberForm as BaseCollectionMemberForm, CollectionChoiceField as CollectionChoiceField, collection_member_permission_formset_factory as collection_member_permission_formset_factory
from wagtail.admin.forms.tags import validate_tag_length as validate_tag_length
from wagtail.admin.widgets import AdminTagWidget as AdminTagWidget
from wagtail.documents.models import Document as Document
from wagtail.documents.permissions import permission_policy as documents_permission_policy
from wagtail.models import Collection as Collection

def formfield_for_dbfield(db_field, **kwargs): ...

class BaseDocumentForm(BaseCollectionMemberForm):
    permission_policy = documents_permission_policy
    original_file: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def save(self, commit: bool = True): ...
    class Meta:
        widgets: Incomplete
    def clean_tags(self): ...

def get_document_base_form(): ...
def get_document_form(model): ...
def get_document_multi_form(model): ...

GroupDocumentPermissionFormSet: Incomplete
