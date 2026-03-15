from django.contrib.auth.models import Group
from django.utils.functional import cached_property as cached_property
from wagtail import hooks as hooks
from wagtail.admin.ui.tables import TitleColumn as TitleColumn
from wagtail.admin.utils import set_query_params as set_query_params
from wagtail.admin.views import generic as generic
from wagtail.admin.viewsets.model import ModelViewSet as ModelViewSet
from wagtail.admin.widgets.button import HeaderButton as HeaderButton
from wagtail.users.forms import GroupForm as GroupForm
from wagtail.users.forms import GroupPagePermissionFormSet as GroupPagePermissionFormSet

def get_permission_panel_classes(): ...

class PermissionPanelFormsMixin:
    def get_permission_panel_form_kwargs(self, cls): ...
    @cached_property
    def permission_panel_forms(self): ...
    produced_error_message: bool
    def is_valid(self, form): ...
    def process_form(self): ...
    def get_context_data(self, **kwargs): ...

class IndexView(generic.IndexView):
    page_title: str
    add_item_label: str
    search_box_placeholder: str
    search_fields: list[str]
    context_object_name: str
    paginate_by: int
    columns: list[TitleColumn]

class CreateView(PermissionPanelFormsMixin, generic.CreateView):
    page_title: str
    success_message: str
    object: Group
    def post(self, request, *args, **kwargs): ...

class EditView(PermissionPanelFormsMixin, generic.EditView):
    success_message: str
    error_message: str
    context_object_name: str
    @cached_property
    def header_buttons(self): ...
    object: Group
    def post(self, request, *args, **kwargs): ...

class DeleteView(generic.DeleteView):
    success_message: str
    page_title: str
    confirmation_message: str

class GroupViewSet(ModelViewSet):
    icon: str
    model = Group
    ordering: list[str]
    add_to_reference_index: bool
    menu_name: str
    menu_label: str
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
