from collections.abc import Generator

from django.contrib.auth.models import AbstractBaseUser
from wagtail.models.workflows import Task, WorkflowState

TASK_TYPES: list[type[Task]]

def get_concrete_descendants(model_class: type, inclusive: bool = True) -> Generator[type]: ...
def get_task_types(task_class: type | None = None) -> list[type[Task]]: ...
def publish_workflow_state(workflow_state: WorkflowState, user: AbstractBaseUser | None = None) -> None: ...
