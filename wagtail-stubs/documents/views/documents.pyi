from typing import Any

from django.db import models
from django.db.models import QuerySet
from django.http import HttpResponse
from django.utils.functional import cached_property as cached_property

from wagtail.admin import messages as messages
from wagtail.admin.auth import PermissionPolicyChecker as PermissionPolicyChecker
from wagtail.admin.filters import BaseMediaFilterSet as BaseMediaFilterSet
from wagtail.admin.ui.tables import BulkActionsCheckboxColumn as BulkActionsCheckboxColumn, Column as Column, DateColumn as DateColumn, DownloadColumn as DownloadColumn, Table as Table, TitleColumn as TitleColumn, UsageCountColumn as UsageCountColumn
from wagtail.admin.utils import get_valid_next_url_from_request as get_valid_next_url_from_request, set_query_params as set_query_params
from wagtail.admin.views import generic as generic
from wagtail.documents import get_document_model as get_document_model
from wagtail.documents.forms import get_document_form as get_document_form
from wagtail.documents.permissions import permission_policy as permission_policy
from wagtail.models import ReferenceIndex as ReferenceIndex
from wagtail.models.media import Collection

permission_checker: PermissionPolicyChecker
Document: type

class BulkActionsColumn(BulkActionsCheckboxColumn):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_header_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class DocumentTable(Table):
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class DocumentsFilterSet(BaseMediaFilterSet):
    permission_policy = permission_policy
    class Meta:
        model = Document
        fields: list[str]

class IndexView(generic.IndexView):
    permission_policy = permission_policy
    any_permission_required: list[str]
    context_object_name: str
    page_title: str
    header_icon: str
    page_kwarg: str
    paginate_by: int
    index_url_name: str
    index_results_url_name: str
    add_url_name: str
    edit_url_name: str
    template_name: str
    results_template_name: str
    default_ordering: str
    table_class = DocumentTable
    filterset_class = DocumentsFilterSet
    model: type
    add_item_label: str
    show_other_searches: bool
    def get_base_queryset(self) -> QuerySet[models.Model]: ...
    @cached_property
    def needs_usage_count_subquery(self) -> bool: ...
    @cached_property
    def current_collection(self) -> Collection | None: ...
    @cached_property
    def columns(self) -> list[Column]: ...
    @cached_property
    def collections(self) -> QuerySet[Collection] | None: ...
    def get_next_url(self) -> str: ...
    def get_add_url(self) -> str: ...
    def get_edit_url(self, instance: models.Model) -> str: ...
    def get_filterset_kwargs(self) -> dict[str, Any]: ...
    def decorate_paginated_queryset(self, object_list: QuerySet[models.Model]) -> QuerySet[models.Model]: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...

class CreateView(generic.CreateView):
    permission_policy = permission_policy
    index_url_name: str
    add_url_name: str
    edit_url_name: str
    error_message: str
    template_name: str
    header_icon: str
    @cached_property
    def model(self) -> type: ...
    def get_form_class(self) -> type: ...
    def get_form_kwargs(self) -> dict[str, Any]: ...
    def get_initial_form_instance(self) -> models.Model: ...
    def get_success_message(self, instance: models.Model) -> str: ...

class EditView(generic.EditView):
    permission_policy = permission_policy
    pk_url_kwarg: str
    error_message: str
    template_name: str
    index_url_name: str
    edit_url_name: str
    delete_url_name: str
    header_icon: str
    context_object_name: str
    @cached_property
    def model(self) -> type: ...
    def get_form_class(self) -> type: ...
    def get_object(self, queryset: QuerySet[models.Model] | None = None) -> models.Model: ...
    def get_form_kwargs(self) -> dict[str, Any]: ...
    def get_success_message(self) -> str: ...
    @cached_property
    def next_url(self) -> str | None: ...
    def get_success_url(self) -> str: ...
    def get_delete_url(self) -> str: ...
    def render_to_response(self, context: dict[str, Any], **response_kwargs: Any) -> HttpResponse: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...

class DeleteView(generic.DeleteView):
    model: type
    pk_url_kwarg: str
    permission_policy = permission_policy
    permission_required: str
    header_icon: str
    usage_url_name: str
    delete_url_name: str
    index_url_name: str
    page_title: str
    def user_has_permission(self, permission: str) -> bool: ...
    @property
    def confirmation_message(self) -> str: ...
    def get_success_message(self) -> str: ...

class UsageView(generic.UsageView):
    model: type
    pk_url_kwarg: str
    permission_policy = permission_policy
    permission_required: str
    header_icon: str
    index_url_name: str
    edit_url_name: str
    def user_has_permission(self, permission: str) -> bool: ...
    def get_page_subtitle(self) -> str: ...
