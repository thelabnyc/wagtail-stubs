from typing import Any

from _typeshed import Incomplete
from django.db import models
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from wagtail.admin.mail import send_mail as send_mail
from wagtail.admin.panels import FieldPanel as FieldPanel
from wagtail.api import APIField as APIField
from wagtail.contrib.forms.utils import get_field_clean_name as get_field_clean_name
from wagtail.models.orderable import Orderable as Orderable
from wagtail.models.pages import Page as Page

from .forms import BaseForm as BaseForm
from .forms import FormBuilder as FormBuilder
from .forms import WagtailAdminFormPageForm as WagtailAdminFormPageForm

FORM_FIELD_CHOICES: list[tuple[str, str]]

class AbstractFormSubmission(models.Model):
    form_data: Incomplete
    page: Incomplete
    submit_time: Incomplete
    def get_data(self) -> dict[str, Any]: ...
    class Meta:
        abstract: bool
        verbose_name: Incomplete
        verbose_name_plural: Incomplete

class FormSubmission(AbstractFormSubmission): ...

class AbstractFormField(Orderable):
    clean_name: Incomplete
    label: Incomplete
    field_type: Incomplete
    required: Incomplete
    choices: Incomplete
    default_value: Incomplete
    help_text: Incomplete
    panels: Incomplete
    api_fields: Incomplete
    def get_field_clean_name(self) -> str: ...
    def save(self, *args: Any, **kwargs: Any) -> None: ...
    class Meta:
        abstract: bool
        ordering: Incomplete

class FormMixin:
    base_form_class: type[WagtailAdminFormPageForm]
    form_builder: type[FormBuilder]
    submissions_list_view_class: type[Any] | None
    landing_page_template: str
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_form_fields(self) -> QuerySet[AbstractFormField]: ...
    def get_data_fields(self) -> list[tuple[str, str]]: ...
    def get_form_class(self) -> type[BaseForm]: ...
    def get_form_parameters(self) -> dict[str, Any]: ...
    def get_form(self, *args: Any, **kwargs: Any) -> BaseForm: ...
    def get_landing_page_template(self, *args: Any, **kwargs: Any) -> str: ...
    def get_submission_class(self) -> type[AbstractFormSubmission]: ...
    def get_submissions(self) -> QuerySet[AbstractFormSubmission]: ...
    def get_submissions_list_view_class(self) -> type[Any]: ...
    def process_form_submission(self, form: BaseForm) -> AbstractFormSubmission: ...
    def render_landing_page(
        self, request: HttpRequest, form_submission: AbstractFormSubmission | None = None, *args: Any, **kwargs: Any
    ) -> HttpResponse: ...
    def serve_submissions_list_view(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def serve(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...
    preview_modes: list[tuple[str, str]]
    def serve_preview(self, request: HttpRequest, mode_name: str) -> HttpResponse: ...
    def get_preview_context(self, request: HttpRequest, mode_name: str) -> dict[str, Any]: ...

def validate_to_address(value: str) -> None: ...

class AbstractForm(FormMixin, Page):
    class Meta:
        abstract: bool

class EmailFormMixin(models.Model):
    to_address: Incomplete
    from_address: Incomplete
    subject: Incomplete
    def process_form_submission(self, form: BaseForm) -> AbstractFormSubmission: ...
    def send_mail(self, form: BaseForm) -> None: ...
    def render_email(self, form: BaseForm) -> str: ...
    class Meta:
        abstract: bool

class AbstractEmailForm(EmailFormMixin, FormMixin, Page):
    class Meta:
        abstract: bool
