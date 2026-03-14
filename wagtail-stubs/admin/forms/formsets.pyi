from django import forms
from django.forms.formsets import ManagementForm

class BaseFormSetMixin:
    deletion_widget: forms.HiddenInput
    @property
    def attrs(self) -> dict[str, str]: ...
    @property
    def management_form(self) -> ManagementForm: ...
