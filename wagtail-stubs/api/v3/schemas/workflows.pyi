from datetime import datetime
from typing import Any, Literal, TypedDict
from uuid import UUID

from django.contrib.auth.models import AbstractBaseUser
from ninja import Schema
from pydantic import BaseModel, PositiveInt
from wagtail.models import Task, TaskState, Workflow, WorkflowMixin, WorkflowState

from .base import BaseSchema

class WorkflowUserSummarySchema(Schema):
    id: int | str | UUID
    name: str
    @staticmethod
    def resolve_id(obj: AbstractBaseUser) -> int | str | UUID: ...
    @staticmethod
    def resolve_name(obj: AbstractBaseUser) -> str: ...

class WorkflowSummarySchema(Schema):
    id: int
    name: str

class WorkflowTaskSummarySchema(Schema):
    id: int
    name: str
    type: str
    @staticmethod
    def resolve_type(obj: Task) -> str: ...

class WorkflowTaskStateSchema(BaseSchema):
    id: int
    task: WorkflowTaskSummarySchema
    status: Literal["in_progress", "approved", "rejected", "skipped", "cancelled"]
    revision_id: int
    started_at: datetime
    finished_at: datetime | None = ...
    finished_by: WorkflowUserSummarySchema | None = ...
    comment: str

class WorkflowTaskTimelineItemSchema(Schema):
    task: WorkflowTaskSummarySchema
    task_state: WorkflowTaskStateSchema | None = ...

class WorkflowStateSchema(BaseSchema):
    id: int
    workflow: WorkflowSummarySchema
    status: Literal["in_progress", "needs_changes", "approved", "cancelled"]
    created_at: datetime
    requested_by: WorkflowUserSummarySchema | None = ...
    current_task_state: WorkflowTaskStateSchema | None = ...
    task_states: list[WorkflowTaskStateSchema]
    @staticmethod
    def resolve_task_states(obj: WorkflowState) -> list[TaskState]: ...

class _WorkflowTaskTimelineItem(TypedDict):
    task: Task
    task_state: TaskState | None

class WorkflowStateDetailSchema(WorkflowStateSchema):
    tasks: list[WorkflowTaskTimelineItemSchema]
    @staticmethod
    def resolve_tasks(obj: WorkflowState) -> list[_WorkflowTaskTimelineItem]: ...

class WorkflowStatusSchema(Schema):
    workflow: WorkflowSummarySchema | None = ...
    workflow_state: WorkflowStateDetailSchema | None = ...
    allowed_actions: list[str] = ...
    @staticmethod
    def resolve_workflow(obj: WorkflowMixin) -> Workflow | None: ...
    @staticmethod
    def resolve_workflow_state(obj: WorkflowMixin) -> WorkflowState | None: ...
    @staticmethod
    def resolve_allowed_actions(obj: WorkflowMixin, context: dict[str, Any]) -> list[str]: ...

class WorkflowTaskActionSchema(BaseModel):
    comment: str | None = ...
    task_state_id: PositiveInt | None = ...
    def __init__(
        self, *, comment: str | None = None, task_state_id: PositiveInt | None = None, **data: Any
    ) -> None: ...
    def get_form_data(self) -> dict[str, Any]: ...
