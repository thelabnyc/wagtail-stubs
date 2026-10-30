from typing import Any

from django.http import HttpRequest, HttpResponse, HttpResponseBase
from django.views.generic.edit import ModelFormMixin, ProcessFormView
from wagtail.admin.forms.pages import PageViewRestrictionForm as PageViewRestrictionForm
from wagtail.admin.modal_workflow import render_modal_workflow as render_modal_workflow
from wagtail.models import AbstractPage
from wagtail.models.pages import PageViewRestriction as PageViewRestriction
from wagtail.models.view_restrictions import BaseViewRestriction as BaseViewRestriction

Page: type[AbstractPage]

class SetPrivacyView(ModelFormMixin[PageViewRestriction, PageViewRestrictionForm], ProcessFormView):
    form_class = PageViewRestrictionForm
    page: AbstractPage
    restriction: PageViewRestriction | None
    restriction_on_ancestor: PageViewRestriction | None
    object: PageViewRestriction | None
    def dispatch(self, request: HttpRequest, page_id: int, *args: Any, **kwargs: Any) -> HttpResponseBase: ...
    def get_form(self, form_class: type[PageViewRestrictionForm] | None = None) -> PageViewRestrictionForm: ...
    def get_form_kwargs(self) -> dict[str, Any]: ...
    def get_initial(self) -> dict[str, Any]: ...
    def form_valid(self, form: PageViewRestrictionForm) -> HttpResponse: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    def render_to_response(self, context: dict[str, Any], **response_kwargs: Any) -> HttpResponse: ...
