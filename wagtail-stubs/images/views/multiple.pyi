from wagtail.admin.views.generic.base import WagtailAdminTemplateMixin as WagtailAdminTemplateMixin
from wagtail.admin.views.generic.multiple_upload import (
    AddView as BaseAddView,
)
from wagtail.admin.views.generic.multiple_upload import (
    CreateFromUploadView as BaseCreateFromUploadView,
)
from wagtail.admin.views.generic.multiple_upload import (
    DeleteUploadView as BaseDeleteUploadView,
)
from wagtail.admin.views.generic.multiple_upload import (
    DeleteView as BaseDeleteView,
)
from wagtail.admin.views.generic.multiple_upload import (
    EditView as BaseEditView,
)
from wagtail.images import get_image_model as get_image_model
from wagtail.images.forms import get_image_form as get_image_form
from wagtail.images.forms import get_image_multi_form as get_image_multi_form
from wagtail.images.permissions import (
    ImagesPermissionPolicyGetter as ImagesPermissionPolicyGetter,
)
from wagtail.images.permissions import (
    permission_policy as permission_policy,
)
from wagtail.images.utils import (
    find_image_duplicates as find_image_duplicates,
)
from wagtail.images.utils import (
    get_accept_attributes as get_accept_attributes,
)
from wagtail.images.utils import (
    get_allowed_image_extensions as get_allowed_image_extensions,
)

class AddView(WagtailAdminTemplateMixin, BaseAddView):
    permission_policy: ImagesPermissionPolicyGetter
    template_name: str
    header_icon: str
    page_title: str
    index_url_name: str
    edit_object_url_name: str
    delete_object_url_name: str
    edit_object_form_prefix: str
    context_object_name: str
    context_object_id_name: str
    edit_upload_url_name: str
    delete_upload_url_name: str
    edit_upload_form_prefix: str
    context_upload_name: str
    context_upload_id_name: str
    def get_breadcrumbs_items(self): ...
    def get_model(self): ...
    def get_upload_form_class(self): ...
    def get_edit_form_class(self): ...
    def get_confirm_duplicate_upload_response(self, duplicates): ...
    def get_edit_object_response_data(self): ...
    def save_object(self, form): ...
    def get_context_data(self, **kwargs): ...

class EditView(BaseEditView):
    permission_policy = permission_policy
    pk_url_kwarg: str
    edit_object_form_prefix: str
    context_object_name: str
    context_object_id_name: str
    edit_object_url_name: str
    delete_object_url_name: str
    def get_model(self): ...
    def get_edit_form_class(self): ...

class DeleteView(BaseDeleteView):
    permission_policy = permission_policy
    pk_url_kwarg: str
    context_object_id_name: str
    def get_model(self): ...

class CreateFromUploadedImageView(BaseCreateFromUploadView):
    edit_upload_url_name: str
    delete_upload_url_name: str
    upload_pk_url_kwarg: str
    edit_upload_form_prefix: str
    context_object_id_name: str
    context_upload_name: str
    def get_model(self): ...
    def get_edit_form_class(self): ...
    def save_object(self, form) -> None: ...

class DeleteUploadView(BaseDeleteUploadView):
    upload_pk_url_kwarg: str
    def get_model(self): ...
