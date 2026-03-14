from .forms import LocaleForm as LocaleForm
from .utils import get_locale_usage as get_locale_usage
from _typeshed import Incomplete
from django.http import HttpRequest, HttpResponseBase
from typing import Any
from wagtail.admin import messages as messages
from wagtail.admin.ui.tables import Column as Column, TitleColumn as TitleColumn
from wagtail.admin.views import generic as generic
from wagtail.admin.viewsets.model import ModelViewSet as ModelViewSet
from wagtail.coreutils import get_content_languages as get_content_languages
from wagtail.models import Locale as Locale
from wagtail.permissions import locale_permission_policy as locale_permission_policy

class LanguageTitleColumn(TitleColumn):
    cell_template_name: str
    def get_value(self, locale): ...

class LocaleUsageColumn(Column):
    def get_value(self, locale): ...

class IndexView(generic.IndexView):
    page_title: Incomplete
    add_item_label: Incomplete
    context_object_name: str
    queryset: Incomplete
    default_ordering: str
    columns: Incomplete
    def get_add_url(self) -> str | None: ...

class CreateView(generic.CreateView):
    page_title: Incomplete
    success_message: Incomplete
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase: ...

class EditView(generic.EditView):
    success_message: Incomplete
    error_message: Incomplete
    context_object_name: str
    queryset: Incomplete

class DeleteView(generic.DeleteView):
    success_message: Incomplete
    page_title: Incomplete
    confirmation_message: Incomplete
    queryset: Incomplete
    cannot_delete_message: Incomplete
    def can_delete(self, locale): ...
    def get_context_data(self, object=None): ...
    def form_valid(self, form): ...

class LocaleViewSet(ModelViewSet):
    icon: str
    model = Locale
    permission_policy = locale_permission_policy
    add_to_reference_index: bool
    index_view_class = IndexView
    add_view_class = CreateView
    edit_view_class = EditView
    delete_view_class = DeleteView
    copy_view_enabled: bool
    template_prefix: str
    def get_common_view_kwargs(self, **kwargs): ...
    def get_form_class(self, for_update: bool = False): ...
