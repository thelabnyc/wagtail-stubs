from typing import Any

from django.urls import URLPattern
from django.utils.functional import cached_property

from wagtail.admin.filters import WagtailFilterSet
from wagtail.admin.ui.tables import Column
from wagtail.admin.views.pages.choose_parent import ChooseParentView
from wagtail.admin.views.pages.listing import IndexView
from wagtail.admin.viewsets.base import ViewSet
from wagtail.models import Page

class PageListingViewSet(ViewSet):
    index_view_class: type[IndexView]
    choose_parent_view_class: type[ChooseParentView]
    model: type[Page]
    columns: list[Column]
    filterset_class: type[WagtailFilterSet] | None
    def get_common_view_kwargs(self, **kwargs: Any) -> dict[str, Any]: ...
    def get_index_view_kwargs(self, **kwargs: Any) -> dict[str, Any]: ...
    def get_choose_parent_view_kwargs(self, **kwargs: Any) -> dict[str, Any]: ...
    @property
    def index_view(self) -> Any: ...
    @property
    def index_results_view(self) -> Any: ...
    @property
    def choose_parent_view(self) -> Any: ...
    def get_urlpatterns(self) -> list[URLPattern]: ...
