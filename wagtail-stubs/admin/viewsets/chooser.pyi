from collections.abc import Callable
from typing import Any

from django import forms
from django.db import models
from django.http import HttpResponseBase
from django.urls import URLPattern
from django.utils.functional import cached_property
from wagtail.admin.views.generic import chooser as chooser_views
from wagtail.admin.viewsets.base import ViewSet
from wagtail.admin.widgets.chooser import BaseChooser, BaseChooserAdapter
from wagtail.blocks import ChooserBlock
from wagtail.permission_policies import BasePermissionPolicy

class ChooserViewSet(ViewSet):
    model: type[models.Model] | str | None
    icon: str
    choose_one_text: str
    page_title: str | None
    choose_another_text: str
    edit_item_text: str
    per_page: int
    preserve_url_parameters: list[str]
    url_filter_parameters: list[str]
    choose_view_class: type[chooser_views.ChooseView]
    choose_results_view_class: type[chooser_views.ChooseResultsView]
    chosen_view_class: type[chooser_views.ChosenView]
    chosen_multiple_view_class: type[chooser_views.ChosenMultipleView]
    create_view_class: type[chooser_views.CreateView]
    base_widget_class: type[BaseChooser]
    widget_telepath_adapter_class: type[BaseChooserAdapter] | None
    base_block_class: type[ChooserBlock]
    register_widget: bool
    creation_form_class: type[forms.BaseForm] | None
    form_fields: list[str] | None
    exclude_form_fields: list[str] | None
    search_tab_label: str
    create_action_label: str
    create_action_clicked_label: str | None
    creation_tab_label: str | None
    permission_policy: BasePermissionPolicy | None
    def __init__(self, name: str | None = None, **kwargs: Any) -> None: ...
    def get_common_view_kwargs(self, **kwargs: Any) -> dict[str, Any]: ...
    @property
    def choose_view(self) -> Callable[..., HttpResponseBase]: ...
    @property
    def choose_results_view(self) -> Callable[..., HttpResponseBase]: ...
    @property
    def chosen_view(self) -> Callable[..., HttpResponseBase]: ...
    @property
    def chosen_multiple_view(self) -> Callable[..., HttpResponseBase]: ...
    @property
    def create_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def model_name(self) -> str: ...
    @cached_property
    def widget_class(self) -> type[BaseChooser]: ...
    def get_block_class(
        self,
        name: str | None = None,
        module_path: str | None = None,
    ) -> type[ChooserBlock]: ...
    def get_urlpatterns(self) -> list[URLPattern]: ...
    def on_register(self) -> None: ...
