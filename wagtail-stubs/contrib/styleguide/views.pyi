from _typeshed import Incomplete
from django import forms
from django.views.generic.base import TemplateView
from wagtail import hooks as hooks
from wagtail.admin import messages as messages
from wagtail.admin.forms.search import SearchForm as SearchForm
from wagtail.admin.rich_text import get_rich_text_editor_widget as get_rich_text_editor_widget
from wagtail.admin.staticfiles import versioned_static as versioned_static
from wagtail.admin.views.generic import WagtailAdminTemplateMixin as WagtailAdminTemplateMixin
from wagtail.admin.widgets import AdminAutoHeightTextInput as AdminAutoHeightTextInput, AdminDateInput as AdminDateInput, AdminDateTimeInput as AdminDateTimeInput, AdminPageChooser as AdminPageChooser, AdminTimeInput as AdminTimeInput, SwitchInput as SwitchInput
from wagtail.compat import URLField as URLField
from wagtail.documents.widgets import AdminDocumentChooser as AdminDocumentChooser
from wagtail.images.widgets import AdminImageChooser as AdminImageChooser
from wagtail.models import Page as Page
from wagtail.snippets.widgets import AdminSnippetChooser as AdminSnippetChooser

class FakeAdminSnippetChooser(AdminSnippetChooser):
    def get_chooser_modal_url(self): ...

class ExampleForm(forms.Form):
    def __init__(self, *args, **kwargs) -> None: ...
    CHOICES: Incomplete
    text: Incomplete
    auto_height_text: Incomplete
    default_rich_text: Incomplete
    url: Incomplete
    email: Incomplete
    date: Incomplete
    time: Incomplete
    datetime: Incomplete
    select: Incomplete
    long_select: Incomplete
    radio_select: Incomplete
    multiple_select: Incomplete
    multiple_checkbox: Incomplete
    boolean: Incomplete
    switch: Incomplete
    disabled_switch: Incomplete
    page_chooser: Incomplete
    image_chooser: Incomplete
    document_chooser: Incomplete
    snippet_chooser: Incomplete
    @property
    def media(self): ...

icon_id_pattern: Incomplete
icon_comment_pattern: Incomplete

class IndexView(WagtailAdminTemplateMixin, TemplateView):
    template_name: str
    page_title: Incomplete
    header_icon: str
    def get_context_data(self, **kwargs): ...
    def get_icons(self): ...
