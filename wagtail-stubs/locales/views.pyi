from typing import Any

from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponseBase
from wagtail.admin import messages as messages
from wagtail.admin.ui.tables import Column as Column
from wagtail.admin.ui.tables import TitleColumn as TitleColumn
from wagtail.admin.views import generic as generic
from wagtail.admin.viewsets.model import ModelViewSet as ModelViewSet
from wagtail.coreutils import get_content_languages as get_content_languages
from wagtail.models import Locale as Locale
from wagtail.permissions import locale_permission_policy as locale_permission_policy

from .forms import LocaleForm as LocaleForm
from .utils import get_locale_usage as get_locale_usage

class LanguageTitleColumn(TitleColumn):
    cell_template_name: str
    def get_value(self, locale: Any) -> Any: ...

class LocaleUsageColumn(Column):
    def get_value(self, locale: Any) -> str: ...

class IndexView(generic.IndexView):
    page_title: str
    add_item_label: str
    context_object_name: str
    queryset: QuerySet[Locale]
    default_ordering: str
    columns: list[Column]
    def get_add_url(self) -> str | None: ...

class CreateView(generic.CreateView):
    page_title: str
    success_message: str
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase: ...

class EditView(generic.EditView):
    success_message: str
    error_message: str
    context_object_name: str
    queryset: QuerySet[Locale]

class DeleteView(generic.DeleteView):
    success_message: str
    page_title: str
    confirmation_message: str
    queryset: QuerySet[Locale]
    cannot_delete_message: str
    def can_delete(self, locale: Any) -> bool: ...
    def get_context_data(self, object: Any = None) -> dict[str, Any]: ...
    def form_valid(self, form: Any) -> Any: ...

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
