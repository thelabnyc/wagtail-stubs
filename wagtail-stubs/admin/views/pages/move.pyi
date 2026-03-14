from django.views.generic.base import TemplateView
from django.views.generic.edit import FormMixin
from wagtail import hooks as hooks
from wagtail.actions.move_page import MovePageAction as MovePageAction
from wagtail.admin import messages as messages
from wagtail.admin.forms.pages import MoveForm as MoveForm
from wagtail.models import Page as Page

class MoveChooseDestination(TemplateView, FormMixin):
    template_name: str
    form_class = MoveForm
    page_to_move: Page
    page_perms: object
    def setup(self, request, *args, **kwargs) -> None: ...
    def get_form_kwargs(self): ...
    def get_context_data(self, **kwargs): ...
    def form_valid(self, form): ...
    def post(self, request, *args, **kwargs): ...

def move_confirm(request, page_to_move_id, destination_id): ...
