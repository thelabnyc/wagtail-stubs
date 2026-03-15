import django_filters
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.functional import cached_property as cached_property
from wagtail import hooks as hooks
from wagtail.admin.filters import DateRangePickerWidget as DateRangePickerWidget, RelatedFilterMixin as RelatedFilterMixin, WagtailFilterSet as WagtailFilterSet
from wagtail.admin.search import SearchArea as SearchArea
from wagtail.admin.ui.menus import MenuItem as MenuItem
from wagtail.admin.ui.tables import BooleanColumn as BooleanColumn, BulkActionsCheckboxColumn as BulkActionsCheckboxColumn, Column as Column, DateColumn as DateColumn, TitleColumn as TitleColumn
from wagtail.admin.utils import get_user_display_name as get_user_display_name
from wagtail.admin.views import generic as generic
from wagtail.admin.viewsets.model import ModelViewSet as ModelViewSet
from wagtail.admin.widgets.boolean_radio_select import BooleanRadioSelect as BooleanRadioSelect
from wagtail.admin.widgets.button import BaseButton as BaseButton, Button as Button, ButtonWithDropdown as ButtonWithDropdown
from wagtail.compat import AUTH_USER_APP_LABEL as AUTH_USER_APP_LABEL, AUTH_USER_MODEL_NAME as AUTH_USER_MODEL_NAME
from wagtail.search import index as index
from wagtail.users.forms import UserCreationForm as UserCreationForm, UserEditForm as UserEditForm
from wagtail.users.utils import user_can_delete_user as user_can_delete_user

User: type[AbstractBaseUser]
add_user_perm: str
change_user_perm: str
delete_user_perm: str

class UserColumn(TitleColumn):
    cell_template_name: str

class GroupFilter(RelatedFilterMixin, django_filters.ModelMultipleChoiceFilter): ...

class UserFilterSet(WagtailFilterSet):
    is_superuser: django_filters.BooleanFilter
    last_login: django_filters.DateFromToRangeFilter
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None, is_searching: bool = False) -> None: ...
    class Meta:
        model = User
        fields: list[str]

class IndexView(generic.IndexView):
    template_name: str
    results_template_name: str
    add_item_label: str
    context_object_name: str
    page_title: str
    show_other_searches: bool
    @cached_property
    def columns(self): ...
    @cached_property
    def model_fields(self): ...
    @cached_property
    def search_fields(self): ...
    def get_filterset_kwargs(self): ...
    def get_delete_url(self, instance): ...
    def get_list_buttons(self, instance): ...
    def get_base_queryset(self): ...
    def order_queryset(self, queryset): ...

class CreateView(generic.CreateView):
    success_message: str
    page_title: str
    def run_before_hook(self): ...
    def run_after_hook(self): ...

class EditView(generic.EditView):
    success_message: str
    error_message: str
    context_object_name: str
    object: AbstractBaseUser
    can_delete: bool
    editing_self: bool
    def setup(self, request, *args, **kwargs) -> None: ...
    def save_instance(self): ...
    def get_form_kwargs(self): ...
    def run_before_hook(self): ...
    def run_after_hook(self): ...
    def get_page_subtitle(self): ...
    def get_context_data(self, **kwargs): ...

class DeleteView(generic.DeleteView):
    page_title: str
    success_message: str
    context_object_name: str
    object: AbstractBaseUser
    def dispatch(self, request, *args, **kwargs): ...
    def run_before_hook(self): ...
    def run_after_hook(self): ...

class HistoryView(generic.HistoryView):
    def get_page_subtitle(self): ...

class UserViewSet(ModelViewSet):
    icon: str
    model = User
    ordering: str
    add_to_reference_index: bool
    filterset_class = UserFilterSet
    menu_name: str
    menu_label: str
    menu_order: int
    add_to_settings_menu: bool
    index_view_class = IndexView
    add_view_class = CreateView
    edit_view_class = EditView
    delete_view_class = DeleteView
    history_view_class = HistoryView
    template_prefix: str
    def get_form_class(self, for_update: bool = False): ...
    @cached_property
    def search_area_class(self): ...
    def get_search_area(self): ...
    def register_search_area(self) -> None: ...
    def on_register(self) -> None: ...
