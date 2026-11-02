from typing import Any

from django.utils.functional import _StrOrPromise
from wagtail.admin.ui.tables import Column as Column
from wagtail.admin.ui.tables import StatusFlagColumn as StatusFlagColumn
from wagtail.admin.ui.tables import TitleColumn as TitleColumn
from wagtail.admin.views import generic as generic
from wagtail.admin.viewsets.model import ModelViewSet as ModelViewSet
from wagtail.models.sites import Site as Site
from wagtail.sites.forms import SiteForm as SiteForm

class IndexView(generic.IndexView):
    page_title: _StrOrPromise
    add_item_label: str
    context_object_name: str
    default_ordering: str
    columns: list[Column]
    def get_base_queryset(self) -> Any: ...

class CreateView(generic.CreateView):
    page_title: _StrOrPromise
    success_message: str
    error_message: str

class EditView(generic.EditView):
    success_message: str
    error_message: str
    context_object_name: str

class DeleteView(generic.DeleteView):
    success_message: str
    page_title: _StrOrPromise
    confirmation_message: str

class SiteViewSet(ModelViewSet):
    icon: str
    model = Site
    add_to_reference_index: bool
    index_view_class = IndexView
    add_view_class = CreateView
    edit_view_class = EditView
    delete_view_class = DeleteView
    template_prefix: str
    def get_common_view_kwargs(self, **kwargs): ...
    def get_form_class(self, for_update: bool = False): ...
