from _typeshed import Incomplete
from django import forms
from wagtail.admin.forms.collections import BaseCollectionMemberForm as BaseCollectionMemberForm, CollectionChoiceField as CollectionChoiceField, collection_member_permission_formset_factory as collection_member_permission_formset_factory
from wagtail.admin.forms.tags import validate_tag_length as validate_tag_length
from wagtail.admin.widgets import AdminTagWidget as AdminTagWidget
from wagtail.images.fields import WagtailImageField as WagtailImageField
from wagtail.images.formats import get_image_formats as get_image_formats
from wagtail.images.models import Image as Image
from wagtail.images.permissions import permission_policy as images_permission_policy
from wagtail.models import Collection as Collection

def formfield_for_dbfield(db_field, **kwargs): ...

class BaseImageForm(BaseCollectionMemberForm):
    permission_policy = images_permission_policy
    original_file: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def save(self, commit: bool = True): ...
    class Meta:
        widgets: Incomplete
    def clean_tags(self): ...

def get_image_base_form(): ...
def get_image_form(model): ...
def get_image_multi_form(model_class): ...

class ImageInsertionForm(forms.Form):
    format: Incomplete
    image_is_decorative: Incomplete
    alt_text: Incomplete
    def clean_alt_text(self): ...

class URLGeneratorForm(forms.Form):
    filter_method: Incomplete
    width: Incomplete
    height: Incomplete
    closeness: Incomplete

GroupImagePermissionFormSet: Incomplete
