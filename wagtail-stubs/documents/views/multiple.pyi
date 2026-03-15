from typing import Any

from django.db import models
from django.forms import Form

from .. import get_document_model as get_document_model
from ..forms import get_document_form as get_document_form, get_document_multi_form as get_document_multi_form
from ..permissions import permission_policy as permission_policy
from wagtail.admin.views.generic.base import WagtailAdminTemplateMixin as WagtailAdminTemplateMixin
from wagtail.admin.views.generic.multiple_upload import AddView as BaseAddView, CreateFromUploadView as BaseCreateFromUploadView, DeleteUploadView as BaseDeleteUploadView, DeleteView as BaseDeleteView, EditView as BaseEditView

class AddView(WagtailAdminTemplateMixin, BaseAddView):
    permission_policy = permission_policy
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
    def get_breadcrumbs_items(self) -> list[dict[str, str]]: ...
    def get_model(self) -> type[models.Model]: ...
    def get_upload_form_class(self) -> type[Form]: ...
    def get_edit_form_class(self) -> type[Form]: ...
    def save_object(self, form: Form) -> models.Model: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...

class EditView(BaseEditView):
    permission_policy = permission_policy
    pk_url_kwarg: str
    edit_object_form_prefix: str
    context_object_name: str
    context_object_id_name: str
    edit_object_url_name: str
    delete_object_url_name: str
    def get_model(self) -> type[models.Model]: ...
    def get_edit_form_class(self) -> type[Form]: ...

class DeleteView(BaseDeleteView):
    permission_policy = permission_policy
    pk_url_kwarg: str
    context_object_id_name: str
    def get_model(self) -> type[models.Model]: ...

class CreateFromUploadedDocumentView(BaseCreateFromUploadView):
    edit_upload_url_name: str
    delete_upload_url_name: str
    upload_pk_url_kwarg: str
    edit_upload_form_prefix: str
    context_object_id_name: str
    context_upload_name: str
    def get_model(self) -> type[models.Model]: ...
    def get_edit_form_class(self) -> type[Form]: ...
    def save_object(self, form: Form) -> None: ...

class DeleteUploadView(BaseDeleteUploadView):
    upload_pk_url_kwarg: str
    def get_model(self) -> type[models.Model]: ...
