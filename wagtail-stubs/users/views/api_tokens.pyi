from typing import Any, ClassVar

from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import QuerySet
from django.forms import BaseForm, BaseModelForm, CharField, Form, ModelChoiceField
from django.http import HttpRequest, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.utils.functional import _StrOrPromise, cached_property
from wagtail.admin.filters import MultipleUserFilter, WagtailFilterSet
from wagtail.admin.ui.components import MediaContainer
from wagtail.admin.ui.side_panels import StatusSidePanel
from wagtail.admin.ui.tables import Column
from wagtail.admin.views import generic
from wagtail.admin.viewsets.model import ModelViewSet
from wagtail.models import APIToken
import django_filters

class APITokenForm(Form):
    name: CharField
    user: ModelChoiceField[AbstractBaseUser]
    def __init__(self, *args: Any, manageable_users: QuerySet[AbstractBaseUser], **kwargs: Any) -> None: ...

class APITokenFilterSet(WagtailFilterSet):
    declared_filters: ClassVar[dict[str, django_filters.Filter]]
    base_filters: ClassVar[dict[str, django_filters.Filter]]
    user: MultipleUserFilter
    created: django_filters.DateFromToRangeFilter
    last_used_at: django_filters.DateFromToRangeFilter
    revoked: django_filters.BooleanFilter
    def filter_revoked(self, queryset: QuerySet[APIToken], name: str, value: bool | None) -> QuerySet[APIToken]: ...
    class Meta:
        model: type[APIToken]
        fields: list[str]

class TokenManagementQuerysetMixin:
    def get_queryset(self) -> QuerySet[APIToken]: ...

class IndexView(TokenManagementQuerysetMixin, generic.IndexView[APIToken]):
    filterset_class: type[APITokenFilterSet]
    @cached_property
    def columns(self) -> list[Column]: ...
    def get_queryset(self) -> QuerySet[APIToken]: ...

class CreateView(generic.CreateView[APIToken]):
    def get_form_kwargs(self) -> dict[str, Any]: ...
    def form_valid(self, form: BaseForm) -> TemplateResponse: ...
    def get_created_context(self, plaintext: str) -> dict[str, Any]: ...

class APITokenStatusSidePanel(StatusSidePanel):
    object: APIToken
    def get_status_templates(self, context: dict[str, Any]) -> list[str]: ...
    def get_usage_context(self) -> dict[str, Any]: ...

class EditView(TokenManagementQuerysetMixin, generic.EditView[APIToken]):
    delete_item_label: str
    def get_side_panels(self) -> MediaContainer: ...

class RevokeView(TokenManagementQuerysetMixin, generic.DeleteView[APIToken]):
    page_title: _StrOrPromise
    template_name: str
    @property
    def confirmation_message(self) -> str: ...
    def post(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponseRedirect | HttpResponsePermanentRedirect: ...

class APITokenViewSet(ModelViewSet[APIToken]):
    model: type[APIToken]
    icon: str
    menu_label: str
    menu_name: str
    menu_order: int
    add_to_settings_menu: bool
    add_to_reference_index: bool
    copy_view_enabled: bool
    inspect_view_enabled: bool
    template_prefix: str
    form_fields: list[str]
    index_view_class: type[IndexView]
    add_view_class: type[CreateView]
    edit_view_class: type[EditView]
    delete_view_class: type[RevokeView]
    def get_form_class(self, for_update: bool = False) -> type[BaseModelForm[Any] | APITokenForm]: ...  # type: ignore[override]
