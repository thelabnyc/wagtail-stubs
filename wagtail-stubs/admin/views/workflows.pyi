from typing import Any

from django.core.paginator import Page as PaginatorPage
from django.db.models import QuerySet
from django.forms import Form
from django.http import HttpRequest, HttpResponse, HttpResponseBase
from django.http.request import QueryDict
from django.utils.functional import cached_property as cached_property
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from wagtail.admin import messages as messages
from wagtail.admin.auth import PermissionPolicyChecker as PermissionPolicyChecker
from wagtail.admin.filters import (
    MultipleContentTypeFilter as MultipleContentTypeFilter,
)
from wagtail.admin.filters import (
    WagtailFilterSet as WagtailFilterSet,
)
from wagtail.admin.forms.workflows import (
    TaskChooserSearchForm as TaskChooserSearchForm,
)
from wagtail.admin.forms.workflows import (
    WorkflowContentTypeForm as WorkflowContentTypeForm,
)
from wagtail.admin.forms.workflows import (
    WorkflowPagesFormSet as WorkflowPagesFormSet,
)
from wagtail.admin.forms.workflows import (
    get_task_form_class as get_task_form_class,
)
from wagtail.admin.forms.workflows import (
    get_workflow_edit_handler as get_workflow_edit_handler,
)
from wagtail.admin.modal_workflow import render_modal_workflow as render_modal_workflow
from wagtail.admin.panels.base import Panel
from wagtail.admin.ui.tables import BaseColumn as BaseColumn
from wagtail.admin.ui.tables import Column as Column
from wagtail.admin.ui.tables import TitleColumn as TitleColumn
from wagtail.admin.views.generic import (
    CreateView as CreateView,
)
from wagtail.admin.views.generic import (
    DeleteView as DeleteView,
)
from wagtail.admin.views.generic import (
    EditView as EditView,
)
from wagtail.admin.views.generic import (
    IndexView as IndexView,
)
from wagtail.admin.views.generic.base import BaseListingView as BaseListingView
from wagtail.admin.views.generic.permissions import PermissionCheckedMixin as PermissionCheckedMixin
from wagtail.admin.views.pages.listing import PageListingMixin as PageListingMixin
from wagtail.admin.widgets.button import Button
from wagtail.coreutils import resolve_model_string as resolve_model_string
from wagtail.models.pages import Page as Page
from wagtail.models.workflows import Task as Task
from wagtail.models.workflows import TaskState as TaskState
from wagtail.models.workflows import Workflow as Workflow
from wagtail.models.workflows import WorkflowState as WorkflowState
from wagtail.models.workflows import WorkflowTask as WorkflowTask
from wagtail.permissions import (
    page_permission_policy as page_permission_policy,
)
from wagtail.permissions import (
    task_permission_policy as task_permission_policy,
)
from wagtail.permissions import (
    workflow_permission_policy as workflow_permission_policy,
)
from wagtail.snippets.models import get_workflow_enabled_models as get_workflow_enabled_models
from wagtail.workflows import get_task_types as get_task_types
import django_filters

task_permission_checker: PermissionPolicyChecker

class WorkflowTitleColumn(TitleColumn):
    cell_template_name: str

class WorkflowUsedByColumn(TitleColumn):
    cell_template_name: str
    def get_cell_context_data(self, instance: Workflow, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class WorkflowTasksColumn(BaseColumn):
    cell_template_name: str
    num_tasks: int
    def get_cell_context_data(self, instance: Workflow, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class BaseWorkflowFilterSet(WagtailFilterSet):
    show_disabled: django_filters.ChoiceFilter
    def __init__(
        self,
        data: QueryDict | None = None,
        queryset: QuerySet | None = None,
        *,
        request: HttpRequest | None = None,
        prefix: str | None = None,
    ) -> None: ...
    def filter_show_disabled(self, queryset: QuerySet, name: str, value: str) -> QuerySet: ...

class WorkflowFilterSet(BaseWorkflowFilterSet):
    class Meta:
        model = Workflow
        fields: list[str]

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
    page_title: str
    add_item_label: str
    header_icon: str
    columns: list[TitleColumn | BaseColumn]
    default_ordering: str
    search_fields: list[str]
    filterset_class = WorkflowFilterSet
    paginate_by: int
    def show_disabled(self) -> bool: ...
    def get_base_queryset(self) -> QuerySet[Workflow]: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...

class Create(CreateView):
    permission_policy = workflow_permission_policy
    model = Workflow
    page_title: str
    template_name: str
    success_message: str
    add_url_name: str
    edit_url_name: str
    index_url_name: str
    header_icon: str
    edit_handler: Panel | None
    def get_edit_handler(self) -> Panel: ...
    def get_form_class(self) -> type[Form]: ...
    def get_initial_form_instance(self) -> Workflow: ...
    def get_pages_formset(self) -> WorkflowPagesFormSet: ...
    def get_content_type_form(self) -> WorkflowContentTypeForm: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    pages_formset: WorkflowPagesFormSet
    content_type_form: WorkflowContentTypeForm
    produced_error_message: bool
    def is_valid(self, form: Form) -> bool: ...
    form: Form
    object: Workflow
    def form_valid(self, form: Form) -> HttpResponseBase: ...

class Edit(EditView):
    permission_policy = workflow_permission_policy
    model = Workflow
    page_title: str
    template_name: str
    success_message: str
    add_url_name: str
    edit_url_name: str
    delete_url_name: str
    delete_item_label: str
    index_url_name: str
    enable_item_label: str
    enable_url_name: str
    header_icon: str
    header_more_buttons: list[Button]
    edit_handler: Panel | None
    MAX_PAGES: int
    def get_edit_handler(self) -> Panel: ...
    def get_form_class(self) -> type[Form]: ...
    def get_pages_formset(self) -> WorkflowPagesFormSet: ...
    def get_content_type_form(self) -> WorkflowContentTypeForm: ...
    def get_paginated_pages(self) -> PaginatorPage[Page]: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    @property
    def get_enable_url(self) -> str: ...
    pages_formset: WorkflowPagesFormSet
    content_type_form: WorkflowContentTypeForm
    produced_error_message: bool
    def is_valid(self, form: Form) -> bool: ...
    form: Form
    object: Workflow
    def form_valid(self, form: Form) -> HttpResponseBase: ...

class Disable(DeleteView):
    permission_policy = workflow_permission_policy
    model = Workflow
    page_title: str
    template_name: str
    success_message: str
    add_url_name: str
    edit_url_name: str
    delete_url_name: str
    index_url_name: str
    header_icon: str
    @property
    def get_edit_url(self) -> str: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    def delete_action(self) -> None: ...

class WorkflowUsageView(PageListingMixin, PermissionCheckedMixin, BaseListingView):
    permission_policy = workflow_permission_policy
    any_permission_required: set[str]
    pk_url_kwarg: str
    index_url_name: str
    index_results_url_name: str
    paginate_by: int
    header_icon: str
    page_title: str
    object: Workflow
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase: ...
    def get_page_subtitle(self) -> str: ...
    def get_breadcrumbs_items(self) -> list[dict[str, str]]: ...
    def get_index_url(self) -> str: ...
    def get_index_results_url(self) -> str: ...
    def get_object(self) -> Workflow: ...
    def get_base_queryset(self) -> QuerySet[Page]: ...

@require_POST
def enable_workflow(request: HttpRequest, pk: int) -> HttpResponse: ...
@require_POST
def remove_workflow(request: HttpRequest, page_pk: int, workflow_pk: int | None = None) -> HttpResponse: ...

class TaskTitleColumn(TitleColumn):
    cell_template_name: str

class TaskUsageColumn(Column):
    cell_template_name: str

class TaskFilterSet(BaseWorkflowFilterSet):
    def __init__(
        self,
        data: QueryDict | None = None,
        queryset: QuerySet | None = None,
        *,
        request: HttpRequest | None = None,
        prefix: str | None = None,
    ) -> None: ...
    class Meta:
        model = Task
        fields: list[str]

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
    page_title: str
    add_item_label: str
    header_icon: str
    columns: list[TitleColumn | Column]
    default_ordering: str
    search_fields: list[str]
    filterset_class = TaskFilterSet
    paginate_by: int
    def show_disabled(self) -> bool: ...
    def get_queryset(self) -> QuerySet[Task]: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...

def select_task_type(request: HttpRequest) -> HttpResponse: ...

class CreateTask(CreateView):
    permission_policy = task_permission_policy
    page_title: str
    template_name: str
    success_message: str
    add_url_name: str
    edit_url_name: str
    index_url_name: str
    header_icon: str
    @cached_property
    def model(self) -> type[Task]: ...
    def get_form_class(self) -> type[Form]: ...
    def get_add_url(self) -> str: ...
    def get_breadcrumbs_items(self) -> list[dict[str, str]]: ...

class EditTask(EditView):
    permission_policy = task_permission_policy
    template_name: str
    success_message: str
    add_url_name: str
    edit_url_name: str
    delete_url_name: str
    index_url_name: str
    delete_item_label: str
    enable_item_label: str
    enable_url_name: str
    header_icon: str
    header_more_buttons: list[Button]
    @cached_property
    def model(self) -> type[Task]: ...
    @cached_property
    def page_title(self) -> str: ...
    def get_queryset(self) -> QuerySet[Task] | None: ...
    def get_object(self, queryset: QuerySet[Task] | None = None) -> Task: ...
    def get_form_class(self) -> type[Form]: ...
    def get_breadcrumbs_items(self) -> list[dict[str, str]]: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    @property
    def get_enable_url(self) -> str: ...

class DisableTask(DeleteView):
    permission_policy = task_permission_policy
    model = Task
    page_title: str
    template_name: str
    success_message: str
    add_url_name: str
    edit_url_name: str
    delete_url_name: str
    index_url_name: str
    header_icon: str
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    @property
    def get_edit_url(self) -> str: ...
    def delete_action(self) -> None: ...

@require_POST
def enable_task(request: HttpRequest, pk: int) -> HttpResponse: ...
def get_task_chosen_response(request: HttpRequest, task: Task) -> HttpResponse: ...

class BaseTaskChooserView(TemplateView):
    task_models: list[type[Task]]
    can_create: bool
    def dispatch(self, request: HttpRequest) -> HttpResponseBase: ...
    def get_create_model(self) -> type[Task] | None: ...
    create_model: type[Task] | None
    def get_create_form_class(self) -> type[Form] | None: ...
    def get_create_form(self) -> Form | None: ...
    def get_task_type_options(self) -> list[tuple[str, str, str, str]]: ...
    def get_task_type_filter_choices(self) -> list[tuple[type[Task], str]]: ...
    def get_form_js_context(self) -> dict[str, Any]: ...
    def get_task_listing_context_data(self) -> dict[str, Any]: ...
    def get_create_tab_context_data(self) -> dict[str, Any]: ...

class TaskChooserView(BaseTaskChooserView):
    create_form: Form | None
    def get(self, request: HttpRequest) -> HttpResponse: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    def render_to_response(self, context: dict[str, Any]) -> HttpResponse: ...

class TaskChooserCreateView(BaseTaskChooserView):
    create_form: Form | None
    def get(self, request: HttpRequest) -> HttpResponse: ...
    def post(self, request: HttpRequest) -> HttpResponse: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    def render_to_response(self, context: dict[str, Any]) -> HttpResponse: ...

class TaskChooserResultsView(BaseTaskChooserView):
    template_name: str
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...

def task_chosen(request: HttpRequest, task_id: int) -> HttpResponse: ...
