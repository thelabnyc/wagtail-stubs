from collections.abc import Callable, Iterable
from typing import Any, Generic

from django.http import HttpResponseBase
from django.urls import URLPattern
from django.utils.functional import cached_property, classproperty
from typing_extensions import TypeVar
from wagtail.admin.ui.tables import BaseColumn
from wagtail.admin.views.page_privacy import SetPrivacyView
from wagtail.admin.views.pages.choose_parent import ChooseParentView, GenericChooseParentView
from wagtail.admin.views.pages.convert_alias import ConvertAliasView
from wagtail.admin.views.pages.copy import CopyView
from wagtail.admin.views.pages.create import AddSubpageView, CreateView
from wagtail.admin.views.pages.delete import DeleteView
from wagtail.admin.views.pages.edit import EditView
from wagtail.admin.views.pages.history import PageHistoryView, WorkflowHistoryDetailView, WorkflowHistoryView
from wagtail.admin.views.pages.listing import ExplorableIndexView, IndexView, PageFilterSet
from wagtail.admin.views.pages.lock import LockView, UnlockView
from wagtail.admin.views.pages.move import MoveChooseDestinationView, MoveConfirmView
from wagtail.admin.views.pages.ordering import SetPagePositionView
from wagtail.admin.views.pages.preview import PreviewOnCreateView, PreviewOnEditView, ViewDraftView
from wagtail.admin.views.pages.revisions import (
    RevisionsCompareView,
    RevisionsRevertView,
    RevisionsUnscheduleView,
    RevisionsView,
)
from wagtail.admin.views.pages.search import SearchView
from wagtail.admin.views.pages.unpublish import UnpublishView
from wagtail.admin.views.pages.usage import ContentTypeUseView, UsageView
from wagtail.admin.views.pages.workflow import (
    CollectWorkflowActionDataView,
    ConfirmWorkflowCancellationView,
    PreviewRevisionForTaskView,
    WorkflowActionView,
)
from wagtail.admin.viewsets.base import ViewSet, _Undefined
from wagtail.admin.viewsets.listing import ListingViewSetMixin
from wagtail.models import AbstractPage
from wagtail.utils.registry import ObjectTypeRegistry

Page: type[AbstractPage]
_PageT = TypeVar("_PageT", bound=AbstractPage, default=AbstractPage)

class PageListingViewSet(ListingViewSetMixin, ViewSet, Generic[_PageT]):
    index_view_class: type[IndexView[Any]]
    choose_parent_view_class: type[ChooseParentView[Any]]
    model: type[_PageT]
    @classproperty
    def columns(cls) -> list[BaseColumn] | _Undefined: ...
    @classproperty
    def filterset_class(cls) -> type[PageFilterSet] | _Undefined: ...
    @cached_property
    def export_filename(self) -> str: ...
    def get_common_view_kwargs(self, **kwargs: Any) -> dict[str, Any]: ...
    def get_index_view_kwargs(self, **kwargs: Any) -> dict[str, Any]: ...
    def get_choose_parent_view_kwargs(self, **kwargs: Any) -> dict[str, Any]: ...
    @cached_property
    def index_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def index_results_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def choose_parent_view(self) -> Callable[..., HttpResponseBase]: ...
    def get_urlpatterns(self) -> list[URLPattern]: ...

class PageViewSet(PageListingViewSet[_PageT]):
    choose_parent_view_class: type[GenericChooseParentView[Any]]
    content_type_use_view_class: type[ContentTypeUseView]
    add_view_class: type[CreateView[Any]]
    add_subpage_view_class: type[AddSubpageView]
    collect_workflow_action_data_view_class: type[CollectWorkflowActionDataView[Any]]
    confirm_workflow_cancellation_view_class: type[ConfirmWorkflowCancellationView[Any]]
    convert_alias_view_class: type[ConvertAliasView[Any]]
    copy_view_class: type[CopyView]
    delete_view_class: type[DeleteView[Any]]
    edit_view_class: type[EditView[Any]]
    history_view_class: type[PageHistoryView[Any]]
    lock_view_class: type[LockView[Any]]
    move_view_class: type[MoveChooseDestinationView]
    move_confirm_view_class: type[MoveConfirmView[Any]]
    preview_on_add_view_class: type[PreviewOnCreateView[Any]]
    preview_on_edit_view_class: type[PreviewOnEditView[Any]]
    revisions_view_class: type[RevisionsView[Any]]
    revisions_compare_view_class: type[RevisionsCompareView[Any]]
    revisions_revert_view_class: type[RevisionsRevertView[Any]]
    revisions_unschedule_view_class: type[RevisionsUnscheduleView[Any]]
    search_view_class: type[SearchView]
    set_page_position_view_class: type[SetPagePositionView]
    set_privacy_view_class: type[SetPrivacyView]
    unlock_view_class: type[UnlockView[Any]]
    unpublish_view_class: type[UnpublishView[Any]]
    usage_view_class: type[UsageView[Any]]
    view_draft_view_class: type[ViewDraftView]
    workflow_action_view_class: type[WorkflowActionView[Any]]
    workflow_history_view_class: type[WorkflowHistoryView[Any]]
    workflow_history_detail_view_class: type[WorkflowHistoryDetailView[Any]]
    workflow_preview_view_class: type[PreviewRevisionForTaskView[Any]]
    index_view_class: type[ExplorableIndexView[Any]]
    menu_url: None
    @cached_property
    def views(self) -> dict[str, Callable[..., HttpResponseBase]]: ...
    def get_view_by_name(self, name: str) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def content_type_use_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def content_type_use_results_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def add_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def add_subpage_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def collect_workflow_action_data_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def confirm_workflow_cancellation_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def convert_alias_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def copy_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def delete_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def edit_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def history_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def history_results_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def lock_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def move_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def move_confirm_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def preview_on_add_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def preview_on_edit_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def revisions_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def revisions_compare_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def revisions_revert_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def revisions_unschedule_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def search_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def search_results_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def set_page_position_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def set_privacy_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def unlock_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def unpublish_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def usage_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def view_draft_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def workflow_action_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def workflow_history_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def workflow_history_detail_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def workflow_preview_view(self) -> Callable[..., HttpResponseBase]: ...
    @cached_property
    def parent_models(self) -> list[type[AbstractPage]]: ...
    def get_url_name(self, view_name: str) -> _Undefined: ...  # type: ignore[override]
    def get_urlpatterns(self) -> list[URLPattern]: ...
    def on_register(self) -> None: ...

class PageViewSetRegistry(ObjectTypeRegistry):
    values_by_parent_model: dict[type[AbstractPage], PageViewSet[Any]]
    def __init__(self) -> None: ...
    def get_content_type_id_by_page_id(self, page_id: int) -> int: ...
    def get_page_model_by_content_type_id(self, content_type_id: int) -> type[AbstractPage]: ...
    def get_by_parent_model(self, cls: type[AbstractPage]) -> PageViewSet[Any] | None: ...
    def get_by_page_id(self, page_id: int) -> PageViewSet[Any]: ...
    def get_by_parent_page_id(self, parent_page_id: int) -> PageViewSet[Any] | None: ...
    def get_by_content_type_natural_key(self, app_label: str, model_name: str) -> PageViewSet[Any]: ...
    def register(
        self,
        cls: type[AbstractPage],
        value: PageViewSet[Any] | None = None,
        exact_class: bool = False,
        parent_models: Iterable[type[AbstractPage]] = (),
    ) -> None: ...
    def as_view(
        self,
        view_name: str,
        page_id_kwarg: str | None = None,
        parent_page_id_kwarg: str | None = None,
        app_label_kwarg: str | None = None,
        model_name_kwarg: str | None = None,
        is_base_page: bool = False,
    ) -> Callable[..., HttpResponseBase]: ...

page_viewset_registry: PageViewSetRegistry
base_page_viewset: PageViewSet[AbstractPage]
