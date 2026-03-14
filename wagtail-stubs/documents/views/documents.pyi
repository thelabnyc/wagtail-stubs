from _typeshed import Incomplete
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

permission_checker: Incomplete
Document: Incomplete

class BulkActionsColumn(BulkActionsCheckboxColumn):
    def __init__(self, *args, **kwargs) -> None: ...
    def get_header_context_data(self, parent_context): ...

class DocumentTable(Table):
    def get_context_data(self, parent_context): ...

class DocumentsFilterSet(BaseMediaFilterSet):
    permission_policy = permission_policy
    class Meta:
        model = Document
        fields: Incomplete

class IndexView(generic.IndexView):
    permission_policy = permission_policy
    any_permission_required: Incomplete
    context_object_name: str
    page_title: Incomplete
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
    model: Incomplete
    add_item_label: Incomplete
    show_other_searches: bool
    def get_base_queryset(self): ...
    @cached_property
    def needs_usage_count_subquery(self): ...
    @cached_property
    def current_collection(self): ...
    @cached_property
    def columns(self): ...
    @cached_property
    def collections(self): ...
    def get_next_url(self): ...
    def get_add_url(self): ...
    def get_edit_url(self, instance): ...
    def get_filterset_kwargs(self): ...
    def decorate_paginated_queryset(self, object_list): ...
    def get_context_data(self, **kwargs): ...

class CreateView(generic.CreateView):
    permission_policy = permission_policy
    index_url_name: str
    add_url_name: str
    edit_url_name: str
    error_message: Incomplete
    template_name: str
    header_icon: str
    @cached_property
    def model(self): ...
    def get_form_class(self): ...
    def get_form_kwargs(self): ...
    def get_initial_form_instance(self): ...
    def get_success_message(self, instance): ...

class EditView(generic.EditView):
    permission_policy = permission_policy
    pk_url_kwarg: str
    error_message: Incomplete
    template_name: str
    index_url_name: str
    edit_url_name: str
    delete_url_name: str
    header_icon: str
    context_object_name: str
    @cached_property
    def model(self): ...
    def get_form_class(self): ...
    def get_object(self, queryset=None): ...
    def get_form_kwargs(self): ...
    def get_success_message(self): ...
    @cached_property
    def next_url(self): ...
    def get_success_url(self): ...
    def get_delete_url(self): ...
    def render_to_response(self, context, **response_kwargs): ...
    def get_context_data(self, **kwargs): ...

class DeleteView(generic.DeleteView):
    model: Incomplete
    pk_url_kwarg: str
    permission_policy = permission_policy
    permission_required: str
    header_icon: str
    usage_url_name: str
    delete_url_name: str
    index_url_name: str
    page_title: Incomplete
    def user_has_permission(self, permission): ...
    @property
    def confirmation_message(self): ...
    def get_success_message(self): ...

class UsageView(generic.UsageView):
    model: Incomplete
    pk_url_kwarg: str
    permission_policy = permission_policy
    permission_required: str
    header_icon: str
    index_url_name: str
    edit_url_name: str
    def user_has_permission(self, permission): ...
    def get_page_subtitle(self): ...
