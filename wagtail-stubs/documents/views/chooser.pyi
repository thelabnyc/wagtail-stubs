from typing import Any

from django import forms
from django.db import models
from django.db.models import QuerySet
from django.forms import Form
from django.http import HttpRequest, HttpResponse
from django.utils.functional import cached_property as cached_property
from django.views.generic.base import View

from wagtail.admin.staticfiles import versioned_static as versioned_static
from wagtail.admin.ui.tables import Column as Column, DateColumn as DateColumn, DownloadColumn as DownloadColumn
from wagtail.admin.views.generic.chooser import BaseChooseView as BaseChooseView, ChooseResultsViewMixin as ChooseResultsViewMixin, ChooseViewMixin as ChooseViewMixin, ChosenResponseMixin as ChosenResponseMixin, ChosenViewMixin as ChosenViewMixin, CreateViewMixin as CreateViewMixin, CreationFormMixin as CreationFormMixin
from wagtail.admin.viewsets.chooser import ChooserViewSet as ChooserViewSet
from wagtail.admin.widgets import BaseChooser as BaseChooser, BaseChooserAdapter as BaseChooserAdapter
from wagtail.blocks import ChooserBlock as ChooserBlock
from wagtail.documents import get_document_model as get_document_model, get_document_model_string as get_document_model_string
from wagtail.documents.permissions import permission_policy as permission_policy
from wagtail.models.media import Collection

class DocumentChosenResponseMixin(ChosenResponseMixin):
    def get_chosen_response_data(self, document: models.Model) -> dict[str, Any]: ...

class DocumentCreationFormMixin(CreationFormMixin):
    creation_tab_id: str
    def get_creation_form_class(self) -> type: ...
    def get_creation_form_kwargs(self) -> dict[str, Any]: ...

class BaseDocumentChooseView(BaseChooseView):
    results_template_name: str
    per_page: int
    ordering: str
    construct_queryset_hook_name: str
    def get_object_list(self) -> QuerySet[models.Model]: ...
    def get_filter_form(self) -> Form: ...
    @cached_property
    def collections(self) -> QuerySet[Collection] | None: ...
    @property
    def columns(self) -> list[Column]: ...
    model: type
    def get(self, request: HttpRequest) -> HttpResponse: ...

class DocumentChooseViewMixin(ChooseViewMixin):
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...

class DocumentChooseView(DocumentChooseViewMixin, DocumentCreationFormMixin, BaseDocumentChooseView): ...
class DocumentChooseResultsView(ChooseResultsViewMixin, DocumentCreationFormMixin, BaseDocumentChooseView): ...

class DocumentChosenView(ChosenViewMixin, DocumentChosenResponseMixin, View):
    model: type
    def get(self, request: HttpRequest, *args: Any, pk: int | str, **kwargs: Any) -> HttpResponse: ...

class DocumentChooserUploadView(CreateViewMixin, DocumentCreationFormMixin, DocumentChosenResponseMixin, View):
    model: type
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...

class BaseAdminDocumentChooser(BaseChooser):
    classname: str
    js_constructor: str
    model: str
    def __init__(self, **kwargs: Any) -> None: ...
    @property
    def media(self) -> forms.Media: ...

class DocumentChooserAdapter(BaseChooserAdapter):
    js_constructor: str
    @cached_property
    def media(self) -> forms.Media: ...

class BaseDocumentChooserBlock(ChooserBlock):
    def render_basic(self, value: models.Model | None, context: dict[str, Any] | None = None) -> str: ...

class DocumentChooserViewSet(ChooserViewSet):
    choose_view_class = DocumentChooseView
    choose_results_view_class = DocumentChooseResultsView
    chosen_view_class = DocumentChosenView
    create_view_class = DocumentChooserUploadView
    base_widget_class = BaseAdminDocumentChooser
    widget_telepath_adapter_class = DocumentChooserAdapter
    base_block_class = BaseDocumentChooserBlock
    permission_policy = permission_policy
    icon: str
    choose_one_text: str
    create_action_label: str
    create_action_clicked_label: str
    choose_another_text: str
    edit_item_text: str

viewset: DocumentChooserViewSet
