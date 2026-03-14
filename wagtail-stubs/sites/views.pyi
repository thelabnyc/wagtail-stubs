from _typeshed import Incomplete
from wagtail.admin.ui.tables import Column as Column, StatusFlagColumn as StatusFlagColumn, TitleColumn as TitleColumn
from wagtail.admin.views import generic as generic
from wagtail.admin.viewsets.model import ModelViewSet as ModelViewSet
from wagtail.models import Site as Site
from wagtail.permissions import site_permission_policy as site_permission_policy
from wagtail.sites.forms import SiteForm as SiteForm

class IndexView(generic.IndexView):
    page_title: Incomplete
    add_item_label: Incomplete
    context_object_name: str
    default_ordering: str
    columns: Incomplete
    def get_base_queryset(self): ...

class CreateView(generic.CreateView):
    page_title: Incomplete
    success_message: Incomplete
    error_message: Incomplete

class EditView(generic.EditView):
    success_message: Incomplete
    error_message: Incomplete
    context_object_name: str

class DeleteView(generic.DeleteView):
    success_message: Incomplete
    page_title: Incomplete
    confirmation_message: Incomplete

class SiteViewSet(ModelViewSet):
    icon: str
    model = Site
    permission_policy = site_permission_policy
    add_to_reference_index: bool
    index_view_class = IndexView
    add_view_class = CreateView
    edit_view_class = EditView
    delete_view_class = DeleteView
    template_prefix: str
    def get_common_view_kwargs(self, **kwargs): ...
    def get_form_class(self, for_update: bool = False): ...
