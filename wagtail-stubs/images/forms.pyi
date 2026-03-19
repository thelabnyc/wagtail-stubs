from django import forms
from django.db.models.fields.files import FieldFile
from django.forms import FileInput
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
from wagtail.images.fields import WagtailImageField as WagtailImageField
from wagtail.images.formats import get_image_formats as get_image_formats
from wagtail.images.models import Image as Image
from wagtail.images.permissions import permission_policy as images_permission_policy
from wagtail.models.media import Collection as Collection

def formfield_for_dbfield(db_field, **kwargs): ...

class BaseImageForm(BaseCollectionMemberForm):
    permission_policy = images_permission_policy
    original_file: FieldFile
    def __init__(self, *args, **kwargs) -> None: ...
    def save(self, commit: bool = True): ...
    class Meta:
        widgets: dict[str, type[AdminTagWidget] | FileInput | forms.HiddenInput]

    def clean_tags(self): ...

def get_image_base_form(): ...
def get_image_form(model): ...
def get_image_multi_form(model_class): ...

class ImageInsertionForm(forms.Form):
    format: forms.ChoiceField
    image_is_decorative: forms.BooleanField
    alt_text: forms.CharField
    def clean_alt_text(self): ...

class URLGeneratorForm(forms.Form):
    filter_method: forms.ChoiceField
    width: forms.IntegerField
    height: forms.IntegerField
    closeness: forms.IntegerField

GroupImagePermissionFormSet: type[forms.BaseFormSet]
