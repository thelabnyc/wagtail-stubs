from typing import Any

from django.db.models import Model
from django.utils.functional import _StrOrPromise, cached_property
from typing_extensions import TypeVar
from wagtail.admin.ui.tables import LiveStatusTagColumn as LiveStatusTagColumn
from wagtail.admin.views.generic.chooser import (
    BaseChooseView as BaseChooseView,
)
from wagtail.admin.views.generic.chooser import (
    ChooseResultsViewMixin as ChooseResultsViewMixin,
)
from wagtail.admin.views.generic.chooser import (
    ChooseViewMixin as ChooseViewMixin,
)
from wagtail.admin.views.generic.chooser import (
    ChosenMultipleView as ChosenMultipleView,
)
from wagtail.admin.views.generic.chooser import (
    ChosenView as ChosenView,
)
from wagtail.admin.views.generic.chooser import (
    CreateView as CreateView,
)
from wagtail.admin.views.generic.chooser import (
    CreationFormMixin as CreationFormMixin,
)
from wagtail.admin.viewsets.chooser import ChooserViewSet as ChooserViewSet
from wagtail.models.draft_state import DraftStateMixin as DraftStateMixin
from wagtail.snippets.widgets import AdminSnippetChooser as AdminSnippetChooser

_ModelT = TypeVar("_ModelT", bound=Model, default=Model)

class BaseSnippetChooseView(BaseChooseView[_ModelT]):
    filter_form_class: None
    page_title: _StrOrPromise
    results_template_name: str
    per_page: int
    @property
    def page_subtitle(self): ...
    @property
    def columns(self): ...
    def get_context_data(self, **kwargs): ...

class ChooseView(ChooseViewMixin, CreationFormMixin[_ModelT], BaseSnippetChooseView[_ModelT]): ...
class ChooseResultsView(ChooseResultsViewMixin, CreationFormMixin[_ModelT], BaseSnippetChooseView[_ModelT]): ...

class SnippetChosenView(ChosenView[_ModelT]):
    response_data_title_key: str

class SnippetChosenMultipleView(ChosenMultipleView[_ModelT]):
    response_data_title_key: str

class SnippetCreateView(CreateView[_ModelT]):
    response_data_title_key: str

class SnippetChooserViewSet(ChooserViewSet[_ModelT]):
    choose_view_class: type[ChooseView[Any]]
    choose_results_view_class: type[ChooseResultsView[Any]]
    chosen_view_class: type[SnippetChosenView[Any]]
    chosen_multiple_view_class: type[SnippetChosenMultipleView[Any]]
    create_view_class: type[SnippetCreateView[Any]]
    base_widget_class: type[AdminSnippetChooser]
    @cached_property
    def widget_class(self) -> type[AdminSnippetChooser]: ...
