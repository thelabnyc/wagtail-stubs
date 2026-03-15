from django.utils.functional import cached_property as cached_property
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
from wagtail.models import DraftStateMixin as DraftStateMixin
from wagtail.snippets.widgets import AdminSnippetChooser as AdminSnippetChooser

class BaseSnippetChooseView(BaseChooseView):
    filter_form_class: None
    page_title: str
    results_template_name: str
    per_page: int
    @property
    def page_subtitle(self): ...
    @property
    def columns(self): ...
    def get_context_data(self, **kwargs): ...

class ChooseView(ChooseViewMixin, CreationFormMixin, BaseSnippetChooseView): ...
class ChooseResultsView(ChooseResultsViewMixin, CreationFormMixin, BaseSnippetChooseView): ...

class SnippetChosenView(ChosenView):
    response_data_title_key: str

class SnippetChosenMultipleView(ChosenMultipleView):
    response_data_title_key: str

class SnippetCreateView(CreateView):
    response_data_title_key: str

class SnippetChooserViewSet(ChooserViewSet):
    choose_view_class: type[ChooseView]
    choose_results_view_class: type[ChooseResultsView]
    chosen_view_class: type[SnippetChosenView]
    chosen_multiple_view_class: type[SnippetChosenMultipleView]
    create_view_class: type[SnippetCreateView]
    @cached_property
    def widget_class(self): ...
