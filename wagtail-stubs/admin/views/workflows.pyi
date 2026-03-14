from _typeshed import Incomplete
from django.utils.functional import cached_property as cached_property
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from wagtail.admin import messages as messages
from wagtail.admin.auth import PermissionPolicyChecker as PermissionPolicyChecker
from wagtail.admin.filters import MultipleContentTypeFilter as MultipleContentTypeFilter, WagtailFilterSet as WagtailFilterSet
from wagtail.admin.forms.workflows import TaskChooserSearchForm as TaskChooserSearchForm, WorkflowContentTypeForm as WorkflowContentTypeForm, WorkflowPagesFormSet as WorkflowPagesFormSet, get_task_form_class as get_task_form_class, get_workflow_edit_handler as get_workflow_edit_handler
from wagtail.admin.modal_workflow import render_modal_workflow as render_modal_workflow
from wagtail.admin.ui.tables import BaseColumn as BaseColumn, Column as Column, TitleColumn as TitleColumn
from wagtail.admin.views.generic import CreateView as CreateView, DeleteView as DeleteView, EditView as EditView, IndexView as IndexView
from wagtail.admin.views.generic.base import BaseListingView as BaseListingView
from wagtail.admin.views.generic.permissions import PermissionCheckedMixin as PermissionCheckedMixin
from wagtail.admin.views.pages.listing import PageListingMixin as PageListingMixin
from wagtail.coreutils import resolve_model_string as resolve_model_string
from wagtail.models import Page as Page, Task as Task, TaskState as TaskState, Workflow as Workflow, WorkflowState as WorkflowState, WorkflowTask as WorkflowTask
from wagtail.permissions import page_permission_policy as page_permission_policy, task_permission_policy as task_permission_policy, workflow_permission_policy as workflow_permission_policy
from wagtail.snippets.models import get_workflow_enabled_models as get_workflow_enabled_models
from wagtail.workflows import get_task_types as get_task_types

task_permission_checker: Incomplete

class WorkflowTitleColumn(TitleColumn):
    cell_template_name: str

class WorkflowUsedByColumn(TitleColumn):
    cell_template_name: str
    def get_cell_context_data(self, instance, parent_context): ...

class WorkflowTasksColumn(BaseColumn):
    cell_template_name: str
    num_tasks: int
    def get_cell_context_data(self, instance, parent_context): ...

class BaseWorkflowFilterSet(WagtailFilterSet):
    show_disabled: Incomplete
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None) -> None: ...
    def filter_show_disabled(self, queryset, name, value): ...

class WorkflowFilterSet(BaseWorkflowFilterSet):
    class Meta:
        model = Workflow
        fields: Incomplete

class Index(IndexView):
    permission_policy = workflow_permission_policy
    model = Workflow
    context_object_name: str
    template_name: str
    results_template_name: str
    add_url_name: str
    edit_url_name: str
    index_url_name: str
    index_results_url_name: str
    page_title: Incomplete
    add_item_label: Incomplete
    header_icon: str
    columns: Incomplete
    default_ordering: str
    search_fields: Incomplete
    filterset_class = WorkflowFilterSet
    paginate_by: int
    def show_disabled(self): ...
    def get_base_queryset(self): ...
    def get_context_data(self, **kwargs): ...

class Create(CreateView):
    permission_policy = workflow_permission_policy
    model = Workflow
    page_title: Incomplete
    template_name: str
    success_message: Incomplete
    add_url_name: str
    edit_url_name: str
    index_url_name: str
    header_icon: str
    edit_handler: Incomplete
    def get_edit_handler(self): ...
    def get_form_class(self): ...
    def get_initial_form_instance(self): ...
    def get_pages_formset(self): ...
    def get_content_type_form(self): ...
    def get_context_data(self, **kwargs): ...
    pages_formset: Incomplete
    content_type_form: Incomplete
    produced_error_message: Incomplete
    def is_valid(self, form): ...
    form: Incomplete
    object: Incomplete
    def form_valid(self, form): ...

class Edit(EditView):
    permission_policy = workflow_permission_policy
    model = Workflow
    page_title: Incomplete
    template_name: str
    success_message: Incomplete
    add_url_name: str
    edit_url_name: str
    delete_url_name: str
    delete_item_label: Incomplete
    index_url_name: str
    enable_item_label: Incomplete
    enable_url_name: str
    header_icon: str
    header_more_buttons: Incomplete
    edit_handler: Incomplete
    MAX_PAGES: int
    def get_edit_handler(self): ...
    def get_form_class(self): ...
    def get_pages_formset(self): ...
    def get_content_type_form(self): ...
    def get_paginated_pages(self): ...
    def get_context_data(self, **kwargs): ...
    @property
    def get_enable_url(self): ...
    pages_formset: Incomplete
    content_type_form: Incomplete
    produced_error_message: Incomplete
    def is_valid(self, form): ...
    form: Incomplete
    object: Incomplete
    def form_valid(self, form): ...

class Disable(DeleteView):
    permission_policy = workflow_permission_policy
    model = Workflow
    page_title: Incomplete
    template_name: str
    success_message: Incomplete
    add_url_name: str
    edit_url_name: str
    delete_url_name: str
    index_url_name: str
    header_icon: str
    @property
    def get_edit_url(self): ...
    def get_context_data(self, **kwargs): ...
    def delete_action(self) -> None: ...

class WorkflowUsageView(PageListingMixin, PermissionCheckedMixin, BaseListingView):
    permission_policy = workflow_permission_policy
    any_permission_required: Incomplete
    pk_url_kwarg: str
    index_url_name: str
    index_results_url_name: str
    paginate_by: int
    header_icon: str
    page_title: Incomplete
    object: Incomplete
    def dispatch(self, request, *args, **kwargs): ...
    def get_page_subtitle(self): ...
    def get_breadcrumbs_items(self): ...
    def get_index_url(self): ...
    def get_index_results_url(self): ...
    def get_object(self): ...
    def get_base_queryset(self): ...

@require_POST
def enable_workflow(request, pk): ...
@require_POST
def remove_workflow(request, page_pk, workflow_pk=None): ...

class TaskTitleColumn(TitleColumn):
    cell_template_name: str

class TaskUsageColumn(Column):
    cell_template_name: str

class TaskFilterSet(BaseWorkflowFilterSet):
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None) -> None: ...
    class Meta:
        model = Task
        fields: Incomplete

class TaskIndex(IndexView):
    permission_policy = task_permission_policy
    model = Task
    context_object_name: str
    template_name: str
    results_template_name: str
    add_url_name: str
    edit_url_name: str
    index_url_name: str
    index_results_url_name: str
    page_title: Incomplete
    add_item_label: Incomplete
    header_icon: str
    columns: Incomplete
    default_ordering: str
    search_fields: Incomplete
    filterset_class = TaskFilterSet
    paginate_by: int
    def show_disabled(self): ...
    def get_queryset(self): ...
    def get_context_data(self, **kwargs): ...

def select_task_type(request): ...

class CreateTask(CreateView):
    permission_policy = task_permission_policy
    page_title: Incomplete
    template_name: str
    success_message: Incomplete
    add_url_name: str
    edit_url_name: str
    index_url_name: str
    header_icon: str
    @cached_property
    def model(self): ...
    def get_form_class(self): ...
    def get_add_url(self): ...
    def get_breadcrumbs_items(self): ...

class EditTask(EditView):
    permission_policy = task_permission_policy
    template_name: str
    success_message: Incomplete
    add_url_name: str
    edit_url_name: str
    delete_url_name: str
    index_url_name: str
    delete_item_label: Incomplete
    enable_item_label: Incomplete
    enable_url_name: str
    header_icon: str
    header_more_buttons: Incomplete
    @cached_property
    def model(self): ...
    @cached_property
    def page_title(self): ...
    def get_queryset(self): ...
    def get_object(self, queryset=None): ...
    def get_form_class(self): ...
    def get_breadcrumbs_items(self): ...
    def get_context_data(self, **kwargs): ...
    @property
    def get_enable_url(self): ...

class DisableTask(DeleteView):
    permission_policy = task_permission_policy
    model = Task
    page_title: Incomplete
    template_name: str
    success_message: Incomplete
    add_url_name: str
    edit_url_name: str
    delete_url_name: str
    index_url_name: str
    header_icon: str
    def get_context_data(self, **kwargs): ...
    @property
    def get_edit_url(self): ...
    def delete_action(self) -> None: ...

@require_POST
def enable_task(request, pk): ...
def get_task_chosen_response(request, task): ...

class BaseTaskChooserView(TemplateView):
    task_models: Incomplete
    can_create: Incomplete
    def dispatch(self, request): ...
    def get_create_model(self): ...
    create_model: Incomplete
    def get_create_form_class(self): ...
    def get_create_form(self): ...
    def get_task_type_options(self): ...
    def get_task_type_filter_choices(self): ...
    def get_form_js_context(self): ...
    def get_task_listing_context_data(self): ...
    def get_create_tab_context_data(self): ...

class TaskChooserView(BaseTaskChooserView):
    create_form: Incomplete
    def get(self, request): ...
    def get_context_data(self, **kwargs): ...
    def render_to_response(self, context): ...

class TaskChooserCreateView(BaseTaskChooserView):
    create_form: Incomplete
    def get(self, request): ...
    def post(self, request): ...
    def get_context_data(self, **kwargs): ...
    def render_to_response(self, context): ...

class TaskChooserResultsView(BaseTaskChooserView):
    template_name: str
    def get_context_data(self, **kwargs): ...

def task_chosen(request, task_id): ...
