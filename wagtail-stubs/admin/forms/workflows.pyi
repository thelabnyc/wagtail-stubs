from typing import Any

from django import forms
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from django.utils.functional import cached_property
from django.utils.safestring import SafeString
from wagtail.admin.forms.formsets import BaseFormSetMixin
from wagtail.admin.panels.group import ObjectList
from wagtail.models import Page, Task, Workflow, WorkflowPage

class TaskChooserSearchForm(forms.Form):
    q: forms.CharField
    task_type_choices: dict[str, type[Task]]
    def __init__(
        self,
        *args: Any,
        task_type_choices: list[tuple[type[Task], str]] | None = None,
        **kwargs: Any,
    ) -> None: ...
    def is_searching(self) -> bool: ...
    @cached_property
    def task_model(self) -> type[Task]: ...
    def specific_task_model_selected(self) -> bool: ...

class WorkflowPageForm(forms.ModelForm[WorkflowPage]):
    page: forms.ModelChoiceField[Page]
    def clean(self) -> None: ...
    def save(self, commit: bool = False) -> None: ...  # type: ignore[override]

    class Meta:
        model: type[WorkflowPage]
        fields: list[str]

class BaseWorkflowPagesFormSet(BaseFormSetMixin, forms.BaseInlineFormSet):
    def clean(self) -> None: ...

class WorkflowContentTypeForm(forms.Form):
    class ContentTypeMultipleChoiceField(forms.ModelMultipleChoiceField):
        def label_from_instance(self, obj: ContentType) -> str: ...

    class CheckboxSelectMultiple(forms.CheckboxSelectMultiple):
        option_template_name: str
        def get_errors_by_id(self, errors: ErrorList) -> dict[int | None, list[ValidationError]]: ...
        def render_with_errors(
            self,
            name: str,
            value: list[str],
            attrs: dict[str, Any] | None = None,
            renderer: BaseRenderer | None = None,
            errors: ErrorList | None = None,
        ) -> SafeString: ...

    content_types: ContentTypeMultipleChoiceField
    workflow: Workflow | None
    def __init__(self, *args: Any, workflow: Workflow | None = None, **kwargs: Any) -> None: ...
    def clean(self) -> None: ...
    def save(self, commit: bool = True) -> None: ...

WorkflowPagesFormSet: type[BaseWorkflowPagesFormSet]

class BaseTaskForm(forms.ModelForm[Task]): ...

def get_task_form_class(task_model: type[Task], for_edit: bool = False) -> type[BaseTaskForm]: ...
def get_workflow_edit_handler() -> ObjectList: ...
