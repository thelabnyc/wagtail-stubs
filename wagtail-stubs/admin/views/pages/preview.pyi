from typing import Any

from django.contrib.contenttypes.models import ContentType
from django.http import HttpRequest, HttpResponseBase, QueryDict
from django.utils.functional import cached_property
from django.views.generic.base import View
from wagtail.admin.forms.pages import WagtailAdminPageForm
from wagtail.admin.views.generic.preview import PreviewOnEdit as GenericPreviewOnEdit
from wagtail.models import AbstractPage

Page: type[AbstractPage]

class ViewDraftView(View):
    def dispatch(self, request: HttpRequest, page_id: int, *args: Any, **kwargs: Any) -> HttpResponseBase: ...

class PreviewOnEditView(GenericPreviewOnEdit):
    def get_object(self) -> AbstractPage: ...
    def get_form(self, query_dict: QueryDict | None) -> WagtailAdminPageForm: ...

class PreviewOnCreateView(PreviewOnEditView):
    @cached_property
    def content_type(self) -> ContentType: ...
    @cached_property
    def parent_object_id(self) -> int: ...
    def get_object(self) -> AbstractPage: ...
    def get_form(self, query_dict: QueryDict | None) -> WagtailAdminPageForm: ...
