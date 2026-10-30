from wagtail.admin import messages as messages
from wagtail.admin.utils import get_latest_str as get_latest_str
from wagtail.admin.views.generic import workflow as workflow
from wagtail.models import AbstractPage

Page: type[AbstractPage]

class WorkflowPageViewMixin:
    model: type[AbstractPage]
    pk_url_kwarg: str
    redirect_url_name: str
    def add_not_in_moderation_error(self) -> None: ...
    def get_context_data(self, **kwargs): ...

class WorkflowActionView(WorkflowPageViewMixin, workflow.WorkflowAction):
    submit_url_name: str

class CollectWorkflowActionDataView(WorkflowPageViewMixin, workflow.CollectWorkflowActionData):
    submit_url_name: str

class ConfirmWorkflowCancellationView(WorkflowPageViewMixin, workflow.ConfirmWorkflowCancellation):
    template_name: str

class PreviewRevisionForTaskView(WorkflowPageViewMixin, workflow.PreviewRevisionForTask):
    def add_error_message(self) -> None: ...
