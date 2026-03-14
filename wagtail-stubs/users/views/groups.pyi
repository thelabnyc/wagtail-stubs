from _typeshed import Incomplete
from django.contrib.auth.models import Group
from django.utils.functional import cached_property as cached_property
from wagtail import hooks as hooks
from wagtail.admin.ui.tables import TitleColumn as TitleColumn
from wagtail.admin.utils import set_query_params as set_query_params
from wagtail.admin.views import generic as generic
from wagtail.admin.viewsets.model import ModelViewSet as ModelViewSet
from wagtail.admin.widgets.button import HeaderButton as HeaderButton
from wagtail.users.forms import GroupForm as GroupForm, GroupPagePermissionFormSet as GroupPagePermissionFormSet

def get_permission_panel_classes(): ...

class PermissionPanelFormsMixin:
    def get_permission_panel_form_kwargs(self, cls): ...
    @cached_property
    def permission_panel_forms(self): ...
    produced_error_message: Incomplete
    def is_valid(self, form): ...
    def process_form(self): ...
    def get_context_data(self, **kwargs): ...

class IndexView(generic.IndexView):
    page_title: Incomplete
    add_item_label: Incomplete
    search_box_placeholder: Incomplete
    search_fields: Incomplete
    context_object_name: str
    paginate_by: int
    columns: Incomplete

class CreateView(PermissionPanelFormsMixin, generic.CreateView):
    page_title: Incomplete
    success_message: Incomplete
    object: Incomplete
    def post(self, request, *args, **kwargs): ...

class EditView(PermissionPanelFormsMixin, generic.EditView):
    success_message: Incomplete
    error_message: Incomplete
    context_object_name: str
    @cached_property
    def header_buttons(self): ...
    object: Incomplete
    def post(self, request, *args, **kwargs): ...

class DeleteView(generic.DeleteView):
    success_message: Incomplete
    page_title: Incomplete
    confirmation_message: Incomplete

class GroupViewSet(ModelViewSet):
    icon: str
    model = Group
    ordering: Incomplete
    add_to_reference_index: bool
    menu_name: str
    menu_label: Incomplete
    menu_order: int
    add_to_settings_menu: bool
    index_view_class = IndexView
    add_view_class = CreateView
    edit_view_class = EditView
    delete_view_class = DeleteView
    copy_view_enabled: bool
    template_prefix: str
    def get_common_view_kwargs(self, **kwargs): ...
    def get_form_class(self, for_update: bool = False): ...
