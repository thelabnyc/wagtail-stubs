from .. import get_document_model as get_document_model
from ..forms import get_document_form as get_document_form, get_document_multi_form as get_document_multi_form
from ..permissions import permission_policy as permission_policy
from _typeshed import Incomplete
from wagtail.admin.views.generic.base import WagtailAdminTemplateMixin as WagtailAdminTemplateMixin
from wagtail.admin.views.generic.multiple_upload import AddView as BaseAddView, CreateFromUploadView as BaseCreateFromUploadView, DeleteUploadView as BaseDeleteUploadView, DeleteView as BaseDeleteView, EditView as BaseEditView

class AddView(WagtailAdminTemplateMixin, BaseAddView):
    permission_policy = permission_policy
    template_name: str
    header_icon: str
    page_title: Incomplete
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

class CreateFromUploadedDocumentView(BaseCreateFromUploadView):
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
