from _typeshed import Incomplete
from django.db import models
from wagtail.admin.mail import send_mail as send_mail
from wagtail.admin.panels import FieldPanel as FieldPanel
from wagtail.api import APIField as APIField
from wagtail.contrib.forms.utils import get_field_clean_name as get_field_clean_name
from wagtail.models.orderable import Orderable as Orderable
from wagtail.models.pages import Page as Page

from .forms import FormBuilder as FormBuilder
from .forms import WagtailAdminFormPageForm as WagtailAdminFormPageForm

FORM_FIELD_CHOICES: Incomplete

class AbstractFormSubmission(models.Model):
    form_data: Incomplete
    page: Incomplete
    submit_time: Incomplete
    def get_data(self): ...
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
    def get_field_clean_name(self): ...
    def save(self, *args, **kwargs) -> None: ...
    class Meta:
        abstract: bool
        ordering: Incomplete

class FormMixin:
    base_form_class = WagtailAdminFormPageForm
    form_builder = FormBuilder
    submissions_list_view_class: Incomplete
    landing_page_template: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def get_form_fields(self): ...
    def get_data_fields(self): ...
    def get_form_class(self): ...
    def get_form_parameters(self): ...
    def get_form(self, *args, **kwargs): ...
    def get_landing_page_template(self, *args, **kwargs): ...
    def get_submission_class(self): ...
    def get_submissions_list_view_class(self): ...
    def process_form_submission(self, form): ...
    def render_landing_page(self, request, form_submission=None, *args, **kwargs): ...
    def serve_submissions_list_view(self, request, *args, **kwargs): ...
    def serve(self, request, *args, **kwargs): ...
    preview_modes: Incomplete
    def serve_preview(self, request, mode_name): ...
    def get_preview_context(self, request, mode_name): ...

def validate_to_address(value) -> None: ...

class AbstractForm(FormMixin, Page):
    class Meta:
        abstract: bool

class EmailFormMixin(models.Model):
    to_address: Incomplete
    from_address: Incomplete
    subject: Incomplete
    def process_form_submission(self, form): ...
    def send_mail(self, form) -> None: ...
    def render_email(self, form): ...
    class Meta:
        abstract: bool

class AbstractEmailForm(EmailFormMixin, FormMixin, Page):
    class Meta:
        abstract: bool
