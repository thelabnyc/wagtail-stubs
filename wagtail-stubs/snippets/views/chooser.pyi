from _typeshed import Incomplete
from django.utils.functional import cached_property as cached_property
from wagtail.admin.ui.tables import LiveStatusTagColumn as LiveStatusTagColumn
from wagtail.admin.views.generic.chooser import BaseChooseView as BaseChooseView, ChooseResultsViewMixin as ChooseResultsViewMixin, ChooseViewMixin as ChooseViewMixin, ChosenMultipleView as ChosenMultipleView, ChosenView as ChosenView, CreateView as CreateView, CreationFormMixin as CreationFormMixin
from wagtail.admin.viewsets.chooser import ChooserViewSet as ChooserViewSet
from wagtail.models import DraftStateMixin as DraftStateMixin
from wagtail.snippets.widgets import AdminSnippetChooser as AdminSnippetChooser

class BaseSnippetChooseView(BaseChooseView):
    filter_form_class: Incomplete
    page_title: Incomplete
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
    choose_view_class = ChooseView
    choose_results_view_class = ChooseResultsView
    chosen_view_class = SnippetChosenView
    chosen_multiple_view_class = SnippetChosenMultipleView
    create_view_class = SnippetCreateView
    @cached_property
    def widget_class(self): ...
