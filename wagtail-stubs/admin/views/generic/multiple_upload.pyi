from typing import Any

from django.db import models
from django.forms import Form
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.generic.base import TemplateView, View

from wagtail.models import UploadedFile
from wagtail.permission_policies import BasePermissionPolicy

from .permissions import PermissionCheckedMixin

class AddView(PermissionCheckedMixin, TemplateView):
    permission_required: str
    edit_form_template_name: str
    model: type[models.Model]
    object: models.Model
    upload_object: UploadedFile
    form: Form
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
    def get_model(self) -> type[models.Model]: ...
    def get_upload_form_class(self) -> type[Form]: ...
    def get_edit_form_class(self) -> type[Form]: ...
    def dispatch(self, request: HttpRequest) -> HttpResponse: ...
    def save_object(self, form: Form) -> models.Model: ...
    def get_edit_object_form_context_data(self) -> dict[str, Any]: ...
    def get_edit_object_response_data(self) -> dict[str, Any]: ...
    def get_edit_upload_form_context_data(self) -> dict[str, Any]: ...
    def get_edit_upload_response_data(self) -> dict[str, Any]: ...
    def get_invalid_response_data(self, form: Form) -> dict[str, Any]: ...
    def post(self, request: HttpRequest) -> JsonResponse | HttpResponseBadRequest: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...

class EditView(View):
    permission_policy: BasePermissionPolicy
    pk_url_kwarg: str
    edit_object_form_prefix: str
    context_object_name: str
    context_object_id_name: str
    edit_object_url_name: str
    delete_object_url_name: str
    http_method_names: list[str]
    edit_form_template_name: str
    model: type[models.Model]
    form_class: type[Form]
    object: models.Model
    def get_model(self) -> type[models.Model]: ...
    def get_edit_form_class(self) -> type[Form]: ...
    def save_object(self, form: Form) -> None: ...
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> JsonResponse: ...

class DeleteView(View):
    permission_policy: BasePermissionPolicy
    pk_url_kwarg: str
    context_object_id_name: str
    http_method_names: list[str]
    model: type[models.Model]
    object: models.Model
    def get_model(self) -> type[models.Model]: ...
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> JsonResponse: ...

class CreateFromUploadView(View):
    edit_upload_url_name: str
    delete_upload_url_name: str
    upload_pk_url_kwarg: str
    edit_upload_form_prefix: str
    context_object_id_name: str
    context_upload_name: str
    http_method_names: list[str]
    edit_form_template_name: str
    model: type[models.Model]
    form_class: type[Form]
    object: models.Model
    upload: UploadedFile
    def get_model(self) -> type[models.Model]: ...
    def get_edit_form_class(self) -> type[Form]: ...
    def save_object(self, form: Form) -> None: ...
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> JsonResponse: ...

class DeleteUploadView(View):
    upload_pk_url_kwarg: str
    http_method_names: list[str]
    def get_model(self) -> type[models.Model]: ...
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> JsonResponse: ...
