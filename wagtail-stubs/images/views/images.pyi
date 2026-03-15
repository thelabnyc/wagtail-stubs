from django.db import models
from django.utils.functional import cached_property as cached_property
from wagtail.admin import messages as messages
from wagtail.admin.auth import PermissionPolicyChecker as PermissionPolicyChecker
from wagtail.admin.filters import BaseMediaFilterSet as BaseMediaFilterSet
from wagtail.admin.ui.tables import (
    BaseColumn as BaseColumn,
)
from wagtail.admin.ui.tables import (
    BulkActionsCheckboxColumn as BulkActionsCheckboxColumn,
)
from wagtail.admin.ui.tables import (
    Column as Column,
)
from wagtail.admin.ui.tables import (
    DateColumn as DateColumn,
)
from wagtail.admin.ui.tables import (
    TitleColumn as TitleColumn,
)
from wagtail.admin.ui.tables import (
    UsageCountColumn as UsageCountColumn,
)
from wagtail.admin.utils import (
    get_valid_next_url_from_request as get_valid_next_url_from_request,
)
from wagtail.admin.utils import (
    set_query_params as set_query_params,
)
from wagtail.admin.views import generic as generic
from wagtail.images import get_image_model as get_image_model
from wagtail.images.exceptions import InvalidFilterSpecError as InvalidFilterSpecError
from wagtail.images.forms import URLGeneratorForm as URLGeneratorForm
from wagtail.images.forms import get_image_form as get_image_form
from wagtail.images.models import Filter as Filter
from wagtail.images.models import SourceImageIOError as SourceImageIOError
from wagtail.images.permissions import permission_policy as permission_policy
from wagtail.images.utils import generate_signature as generate_signature
from wagtail.models import ReferenceIndex as ReferenceIndex
from wagtail.models import Site as Site

permission_checker: PermissionPolicyChecker
Image: type[models.Model]
USAGE_PAGE_SIZE: int

class ImagesFilterSet(BaseMediaFilterSet):
    permission_policy = permission_policy
    class Meta:
        model = Image
        fields: list[str]

class IndexView(generic.IndexView):
    ORDERING_OPTIONS: dict[str, str]
    default_ordering: str
    context_object_name: str
    permission_policy = permission_policy
    any_permission_required: list[str]
    model = Image
    filterset_class = ImagesFilterSet
    show_other_searches: bool
    header_icon: str
    page_title: str
    add_item_label: str
    index_url_name: str
    index_results_url_name: str
    add_url_name: str
    edit_url_name: str
    template_name: str
    results_template_name: str
    def get_paginate_by(self, queryset): ...
    def get_valid_orderings(self): ...
    def get_base_queryset(self): ...
    @cached_property
    def needs_usage_count_subquery(self): ...
    @cached_property
    def current_collection(self): ...
    def get_add_url(self): ...
    def get_filterset_kwargs(self): ...
    def get_next_url(self): ...
    def decorate_paginated_queryset(self, object_list): ...
    def get_context_data(self, **kwargs): ...
    @cached_property
    def layout(self): ...
    @cached_property
    def columns(self): ...

class BulkActionsColumn(BulkActionsCheckboxColumn):
    def __init__(self, *args, **kwargs) -> None: ...
    def get_header_context_data(self, parent_context): ...

class ImagePreviewColumn(BaseColumn):
    cell_template_name: str

class TitleColumnWithFilename(TitleColumn):
    cell_template_name: str

class EditView(generic.EditView):
    permission_policy = permission_policy
    pk_url_kwarg: str
    error_message: str
    template_name: str
    index_url_name: str
    edit_url_name: str
    delete_url_name: str
    url_generator_url_name: str
    header_icon: str
    context_object_name: str
    @cached_property
    def model(self): ...
    def get_form_class(self): ...
    def get_form_kwargs(self): ...
    def get_object(self, queryset=None): ...
    def get_success_message(self): ...
    @cached_property
    def next_url(self): ...
    def get_success_url(self): ...
    def render_to_response(self, context, **response_kwargs): ...
    def get_context_data(self, **kwargs): ...

class URLGeneratorView(generic.InspectView):
    any_permission_required: list[str]
    model: type[models.Model]
    pk_url_kwarg: str
    header_icon: str
    output_only: bool
    page_title: str
    template_name: str
    output_template_name: str
    index_url_name: str
    edit_url_name: str
    invalid_filter_error: str
    def get_page_subtitle(self): ...
    def get_fields(self): ...
    def get_template_names(self): ...
    object: models.Model
    filter_spec: str
    form: URLGeneratorForm
    def get(self, request, image_id, *args, **kwargs): ...
    def get_context_data(self, **kwargs): ...
    def get_filter_spec(self, filter_method, width, height, closeness): ...

def preview(request, image_id, filter_spec): ...

class DeleteView(generic.DeleteView):
    model: type[models.Model]
    pk_url_kwarg: str
    permission_policy = permission_policy
    permission_required: str
    header_icon: str
    template_name: str
    usage_url_name: str
    delete_url_name: str
    index_url_name: str
    page_title: str
    def user_has_permission(self, permission): ...
    @property
    def confirmation_message(self): ...
    def get_success_message(self): ...

class CreateView(generic.CreateView):
    permission_policy = permission_policy
    index_url_name: str
    add_url_name: str
    edit_url_name: str
    error_message: str
    template_name: str
    header_icon: str
    @cached_property
    def model(self): ...
    def get_form_class(self): ...
    def get_form_kwargs(self): ...
    def get_initial_form_instance(self): ...
    def get_success_message(self, instance): ...

class UsageView(generic.UsageView):
    model: type[models.Model]
    paginate_by = USAGE_PAGE_SIZE
    pk_url_kwarg: str
    permission_policy = permission_policy
    permission_required: str
    header_icon: str
    index_url_name: str
    edit_url_name: str
    def get_base_object_queryset(self): ...
    def user_has_permission(self, permission): ...
    def get_page_subtitle(self): ...
