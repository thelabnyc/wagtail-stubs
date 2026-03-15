from collections.abc import Sequence
from typing import Any

from django.contrib.auth.models import AbstractBaseUser
from django.db.models import QuerySet
from django.forms import Form
from django.http import HttpRequest, HttpResponse, HttpResponseBase
from django.views.generic.base import View
from wagtail import hooks as hooks
from wagtail.admin.forms.choosers import (
    AnchorLinkChooserForm as AnchorLinkChooserForm,
)
from wagtail.admin.forms.choosers import (
    EmailLinkChooserForm as EmailLinkChooserForm,
)
from wagtail.admin.forms.choosers import (
    ExternalLinkChooserForm as ExternalLinkChooserForm,
)
from wagtail.admin.forms.choosers import (
    PhoneLinkChooserForm as PhoneLinkChooserForm,
)
from wagtail.admin.forms.search import SearchForm as SearchForm
from wagtail.admin.modal_workflow import render_modal_workflow as render_modal_workflow
from wagtail.admin.ui.tables import BaseColumn as BaseColumn
from wagtail.admin.ui.tables import Column as Column
from wagtail.admin.ui.tables import DateColumn as DateColumn
from wagtail.admin.ui.tables import Table as Table
from wagtail.coreutils import resolve_model_string as resolve_model_string
from wagtail.models import Locale as Locale
from wagtail.models import Page as Page
from wagtail.models import Site as Site

def shared_context(request: HttpRequest, extra_context: dict[str, Any] | None = None) -> dict[str, Any]: ...
def page_models_from_string(string: str) -> tuple[type[Page], ...]: ...
def can_choose_page(
    page: Page,
    user: AbstractBaseUser,
    desired_classes: tuple[type[Page], ...],
    can_choose_root: bool = True,
    user_perm: str | bool | None = None,
    target_pages: QuerySet[Page] | None = None,
    match_subclass: bool = True,
) -> bool: ...

class PageChooserTable(Table):
    classname: str
    show_locale_labels: bool
    def __init__(
        self,
        columns: Sequence[BaseColumn],
        data: Sequence[Page],
        *,
        show_locale_labels: bool = False,
        template_name: str | None = None,
        base_url: str | None = None,
        ordering: str | None = None,
        classname: str | None = None,
        attrs: dict[str, str] | None = None,
        caption: str | None = None,
    ) -> None: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...
    def get_row_classname(self, page: Page) -> str: ...

class PageTitleColumn(Column):
    cell_template_name: str
    is_multiple_choice: bool
    def __init__(
        self,
        name: str,
        *,
        is_multiple_choice: bool = False,
        label: str | None = None,
        accessor: str | None = None,
        classname: str | None = None,
        sort_key: str | None = None,
        width: str | None = None,
        ascending_title_text: str | None = None,
        descending_title_text: str | None = None,
    ) -> None: ...
    def get_value(self, instance: Page) -> str: ...
    def get_cell_context_data(self, instance: Page, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class ParentPageColumn(Column):
    cell_template_name: str
    def get_value(self, instance: Page) -> Page | None: ...
    def get_cell_context_data(self, instance: Page, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class PageStatusColumn(Column):
    cell_template_name: str
    def get_value(self, instance: Page) -> Page: ...

class PageNavigateToChildrenColumn(Column):
    cell_template_name: str
    def get_value(self, instance: Page) -> Page: ...

class PageCheckboxSelectColumn(Column):
    cell_template_name: str

class BrowseView(View):
    @property
    def columns(self) -> list[Column]: ...
    def get_object_list(self) -> QuerySet[Page]: ...
    def filter_object_list(self, pages: QuerySet[Page]) -> QuerySet[Page]: ...
    i18n_enabled: bool
    is_multiple_choice: str | None
    desired_classes: tuple[type[Page], ...]
    parent_page: Page
    def get(self, request: HttpRequest, parent_page_id: int | None = None) -> HttpResponseBase: ...

class SearchView(View):
    @property
    def columns(self) -> list[Column]: ...
    i18n_enabled: bool
    is_multiple_choice: str | None
    def get(self, request: HttpRequest) -> HttpResponse: ...

class ChosenMultipleView(View):
    def render_chosen_response(self, result: list[dict[str, str | int | None]]) -> HttpResponseBase: ...
    def get(self, request: HttpRequest) -> HttpResponseBase: ...

class BaseLinkFormView(View):
    form_prefix: str
    form_class: type[Form]
    template_name: str
    step_name: str
    link_url_field_name: str
    def get_initial_data(self) -> dict[str, str]: ...
    def get_url_from_field_value(self, value: str) -> str: ...
    def get_result_data(self) -> dict[str, str | bool]: ...
    form: Form
    def get(self, request: HttpRequest) -> HttpResponseBase: ...
    def post(self, request: HttpRequest) -> HttpResponseBase: ...
    def render_form_response(self) -> HttpResponseBase: ...
    def render_chosen_response(self, result: dict[str, str | bool]) -> HttpResponseBase: ...

LINK_CONVERSION_ALL: str
LINK_CONVERSION_EXACT: str
LINK_CONVERSION_CONFIRM: str

class ExternalLinkView(BaseLinkFormView):
    form_prefix: str
    form_class = ExternalLinkChooserForm
    template_name: str
    step_name: str
    link_url_field_name: str
    form: ExternalLinkChooserForm
    def post(self, request: HttpRequest) -> HttpResponseBase: ...

class AnchorLinkView(BaseLinkFormView):
    form_prefix: str
    form_class = AnchorLinkChooserForm
    template_name: str
    step_name: str
    link_url_field_name: str
    def get_url_from_field_value(self, value: str) -> str: ...

class EmailLinkView(BaseLinkFormView):
    form_prefix: str
    form_class = EmailLinkChooserForm
    template_name: str
    step_name: str
    link_url_field_name: str
    def get_initial_data(self) -> dict[str, str]: ...
    def get_url_from_field_value(self, value: str) -> str: ...
    def get_result_data(self) -> dict[str, str | bool]: ...
    form: EmailLinkChooserForm
    def post(self, request: HttpRequest) -> HttpResponseBase: ...
    def parse_email_link(self, mailto: str) -> dict[str, str]: ...

class PhoneLinkView(BaseLinkFormView):
    form_prefix: str
    form_class = PhoneLinkChooserForm
    template_name: str
    step_name: str
    link_url_field_name: str
    def get_url_from_field_value(self, value: str) -> str: ...
