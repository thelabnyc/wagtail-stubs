from typing import Generic

from typing_extensions import TypeVar
from wagtail.admin import messages as messages
from wagtail.admin.utils import get_latest_str as get_latest_str
from wagtail.admin.views.generic import workflow as workflow
from wagtail.models import AbstractPage

Page: type[AbstractPage]
_PageT = TypeVar("_PageT", bound=AbstractPage, default=AbstractPage)

class WorkflowPageViewMixin(Generic[_PageT]):
    model: type[_PageT]
    pk_url_kwarg: str
    redirect_url_name: str
    def add_not_in_moderation_error(self) -> None: ...
    def get_context_data(self, **kwargs): ...

class WorkflowActionView(WorkflowPageViewMixin[_PageT], workflow.WorkflowAction[_PageT]):
    submit_url_name: str

class CollectWorkflowActionDataView(WorkflowPageViewMixin[_PageT], workflow.CollectWorkflowActionData[_PageT]):
    submit_url_name: str

class ConfirmWorkflowCancellationView(WorkflowPageViewMixin[_PageT], workflow.ConfirmWorkflowCancellation[_PageT]):
    template_name: str

class PreviewRevisionForTaskView(WorkflowPageViewMixin[_PageT], workflow.PreviewRevisionForTask[_PageT]):
    def add_error_message(self) -> None: ...
