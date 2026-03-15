from typing import Any, ClassVar
import datetime

from django import forms
from django.contrib.auth.models import AbstractBaseUser, Group
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.checks import CheckMessage
from django.db import models
from django.utils.functional import _StrPromise, cached_property
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.forms import TaskStateCommentForm
from wagtail.locks import BaseLock, WorkflowLock
from wagtail.models.orderable import Orderable
from wagtail.models.revisions import Revision
from wagtail.models.specific import SpecificMixin
from wagtail.query import PageQuerySet, SpecificQuerySetMixin

# ---------------------------------------------------------------------------
# WorkflowContentType
# ---------------------------------------------------------------------------

class WorkflowContentType(models.Model):
    content_type: models.OneToOneField[ContentType, ContentType]
    workflow: models.ForeignKey[Workflow, Workflow]

# ---------------------------------------------------------------------------
# WorkflowState QuerySet / Manager / Model
# ---------------------------------------------------------------------------

class WorkflowStateQuerySet(models.QuerySet[WorkflowState]):
    def active(self) -> WorkflowStateQuerySet: ...
    def for_instance(self, instance: models.Model) -> WorkflowStateQuerySet: ...

class WorkflowStateManager(models.Manager[WorkflowState]):
    def active(self) -> WorkflowStateQuerySet: ...
    def for_instance(self, instance: models.Model) -> WorkflowStateQuerySet: ...

class WorkflowState(models.Model):
    STATUS_IN_PROGRESS: ClassVar[str]
    STATUS_APPROVED: ClassVar[str]
    STATUS_NEEDS_CHANGES: ClassVar[str]
    STATUS_CANCELLED: ClassVar[str]
    STATUS_CHOICES: ClassVar[
        tuple[
            tuple[str, _StrPromise],
            tuple[str, _StrPromise],
            tuple[str, _StrPromise],
            tuple[str, _StrPromise],
        ]
    ]

    content_type: models.ForeignKey[ContentType, ContentType]
    base_content_type: models.ForeignKey[ContentType, ContentType]
    object_id: models.CharField[str, str]
    content_object: GenericForeignKey
    workflow: models.ForeignKey[Workflow, Workflow]
    status: models.CharField[str, str]
    created_at: models.DateTimeField[datetime.datetime, datetime.datetime]
    requested_by: models.ForeignKey[AbstractBaseUser | None, AbstractBaseUser | None]
    current_task_state: models.OneToOneField[TaskState | None, TaskState | None]

    on_finish: ClassVar[Any]

    objects: ClassVar[WorkflowStateManager]  # type: ignore[assignment]

    def clean(self) -> None: ...
    def save(self, *args: Any, **kwargs: Any) -> None: ...
    def resume(self, user: AbstractBaseUser | None = None) -> None: ...
    def user_can_cancel(self, user: AbstractBaseUser) -> bool: ...
    def update(
        self,
        user: AbstractBaseUser | None = None,
        next_task: Task | None = None,
    ) -> None: ...
    @property
    def successful_task_states(self) -> models.QuerySet[TaskState]: ...
    def get_next_task(self) -> Task | None: ...
    def cancel(self, user: AbstractBaseUser | None = None) -> None: ...
    def finish(self, user: AbstractBaseUser | None = None) -> None: ...
    def copy_approved_task_states_to_revision(self, revision: Revision) -> None: ...
    def revisions(self) -> models.QuerySet[Revision]: ...
    def all_tasks_with_status(self) -> list[Task]: ...
    def all_tasks_with_state(self) -> list[Task]: ...
    @property
    def is_active(self) -> bool: ...
    @property
    def is_at_final_task(self) -> bool: ...

    class Meta:
        verbose_name: _StrPromise
        verbose_name_plural: _StrPromise

# ---------------------------------------------------------------------------
# Workflow Manager / Abstract / Concrete
# ---------------------------------------------------------------------------

class WorkflowManager(models.Manager[Workflow]):
    def active(self) -> models.QuerySet[Workflow]: ...

class AbstractWorkflow(ClusterableModel):
    name: models.CharField[str, str]
    active: models.BooleanField[bool, bool]
    objects: ClassVar[WorkflowManager]  # type: ignore[assignment]

    @property
    def tasks(self) -> models.QuerySet[Task]: ...
    def start(self, obj: models.Model, user: AbstractBaseUser) -> WorkflowState: ...
    def deactivate(self, user: AbstractBaseUser | None = None) -> None: ...
    def all_pages(self) -> PageQuerySet: ...

    class Meta:
        verbose_name: _StrPromise
        verbose_name_plural: _StrPromise
        abstract: bool

class Workflow(AbstractWorkflow): ...

# ---------------------------------------------------------------------------
# WorkflowTask
# ---------------------------------------------------------------------------

class WorkflowTask(Orderable):
    workflow: ParentalKey[Workflow, Workflow]
    task: models.ForeignKey[Task, Task]

    class Meta(Orderable.Meta):
        unique_together: ClassVar[list[tuple[str, str]]]
        verbose_name: _StrPromise
        verbose_name_plural: _StrPromise

# ---------------------------------------------------------------------------
# Task QuerySet / Manager / Model
# ---------------------------------------------------------------------------

class TaskQuerySet(SpecificQuerySetMixin, models.QuerySet[Task]):
    def active(self) -> TaskQuerySet: ...

class TaskManager(models.Manager[Task]):
    def active(self) -> TaskQuerySet: ...

class Task(SpecificMixin, models.Model):
    name: models.CharField[str, str]
    content_type: models.ForeignKey[ContentType, ContentType]
    active: models.BooleanField[bool, bool]
    objects: ClassVar[TaskManager]  # type: ignore[assignment]

    admin_form_fields: ClassVar[list[str]]
    admin_form_readonly_on_edit_fields: ClassVar[list[str]]
    task_state_class: ClassVar[type[TaskState] | None]

    @property
    def workflows(self) -> models.QuerySet[Workflow]: ...
    @property
    def active_workflows(self) -> models.QuerySet[Workflow]: ...
    @classmethod
    def get_verbose_name(cls) -> str: ...
    @classmethod
    def get_task_state_class(cls) -> type[TaskState]: ...
    def start(
        self,
        workflow_state: WorkflowState,
        user: AbstractBaseUser | None = None,
    ) -> TaskState: ...
    def on_action(
        self,
        task_state: TaskState,
        user: AbstractBaseUser,
        action_name: str,
        **kwargs: Any,
    ) -> None: ...
    def user_can_access_editor(self, obj: models.Model, user: AbstractBaseUser) -> bool: ...
    def locked_for_user(self, obj: models.Model, user: AbstractBaseUser) -> bool: ...
    def user_can_lock(self, obj: models.Model, user: AbstractBaseUser) -> bool: ...
    def user_can_unlock(self, obj: models.Model, user: AbstractBaseUser) -> bool: ...
    def get_actions(self, obj: models.Model, user: AbstractBaseUser) -> list[tuple[str, _StrPromise, bool]]: ...
    def get_form_for_action(self, action: str) -> type[TaskStateCommentForm]: ...
    def get_template_for_action(self, action: str) -> str: ...
    def get_task_states_user_can_moderate(
        self, user: AbstractBaseUser, **kwargs: Any
    ) -> models.QuerySet[TaskState]: ...
    @classmethod
    def get_description(cls) -> str: ...
    def deactivate(self, user: AbstractBaseUser | None = None) -> None: ...

    class Meta:
        verbose_name: _StrPromise
        verbose_name_plural: _StrPromise

# ---------------------------------------------------------------------------
# GroupApprovalTask (abstract + concrete)
# ---------------------------------------------------------------------------

class AbstractGroupApprovalTask(Task):
    groups: models.ManyToManyField[Group, Group]

    admin_form_fields: ClassVar[list[str]]  # type: ignore[assignment]
    admin_form_widgets: ClassVar[dict[str, type[forms.Widget]]]

    def start(
        self,
        workflow_state: WorkflowState,
        user: AbstractBaseUser | None = None,
    ) -> TaskState: ...
    def user_can_access_editor(self, obj: models.Model, user: AbstractBaseUser) -> bool: ...
    def locked_for_user(self, obj: models.Model, user: AbstractBaseUser) -> bool: ...
    def user_can_lock(self, obj: models.Model, user: AbstractBaseUser) -> bool: ...
    def user_can_unlock(self, obj: models.Model, user: AbstractBaseUser) -> bool: ...
    def get_actions(self, obj: models.Model, user: AbstractBaseUser) -> list[tuple[str, _StrPromise, bool]]: ...
    def get_task_states_user_can_moderate(
        self, user: AbstractBaseUser, **kwargs: Any
    ) -> models.QuerySet[TaskState]: ...
    @classmethod
    def get_description(cls) -> _StrPromise: ...  # type: ignore[override]

    class Meta:
        abstract: bool
        verbose_name: _StrPromise
        verbose_name_plural: _StrPromise

class GroupApprovalTask(AbstractGroupApprovalTask): ...

# ---------------------------------------------------------------------------
# TaskState QuerySet / Manager / Model
# ---------------------------------------------------------------------------

class BaseTaskStateManager(models.Manager[TaskState]):
    def reviewable_by(self, user: AbstractBaseUser) -> models.QuerySet[TaskState]: ...

class TaskStateQuerySet(SpecificQuerySetMixin, models.QuerySet[TaskState]):
    def for_instance(self, instance: models.Model) -> TaskStateQuerySet: ...

class TaskStateManager(BaseTaskStateManager):
    def for_instance(self, instance: models.Model) -> TaskStateQuerySet: ...

class TaskState(SpecificMixin, models.Model):
    STATUS_IN_PROGRESS: ClassVar[str]
    STATUS_APPROVED: ClassVar[str]
    STATUS_REJECTED: ClassVar[str]
    STATUS_SKIPPED: ClassVar[str]
    STATUS_CANCELLED: ClassVar[str]
    STATUS_CHOICES: ClassVar[
        tuple[
            tuple[str, _StrPromise],
            tuple[str, _StrPromise],
            tuple[str, _StrPromise],
            tuple[str, _StrPromise],
            tuple[str, _StrPromise],
        ]
    ]

    workflow_state: models.ForeignKey[WorkflowState, WorkflowState]
    revision: models.ForeignKey[Revision, Revision]
    task: models.ForeignKey[Task, Task]
    status: models.CharField[str, str]
    started_at: models.DateTimeField[datetime.datetime, datetime.datetime]
    finished_at: models.DateTimeField[datetime.datetime | None, datetime.datetime | None]
    finished_by: models.ForeignKey[AbstractBaseUser | None, AbstractBaseUser | None]
    comment: models.TextField[str, str]
    content_type: models.ForeignKey[ContentType, ContentType]

    exclude_fields_in_copy: ClassVar[list[str]]
    default_exclude_fields_in_copy: ClassVar[list[str]]

    objects: ClassVar[TaskStateManager]  # type: ignore[assignment]

    def approve(
        self,
        user: AbstractBaseUser | None = None,
        update: bool = True,
        comment: str = "",
    ) -> TaskState: ...
    def reject(
        self,
        user: AbstractBaseUser | None = None,
        update: bool = True,
        comment: str = "",
    ) -> TaskState: ...
    @cached_property
    def task_type_started_at(self) -> datetime.datetime | None: ...
    def cancel(
        self,
        user: AbstractBaseUser | None = None,
        resume: bool = False,
        comment: str = "",
    ) -> TaskState: ...
    def copy(
        self,
        update_attrs: dict[str, Any] | None = None,
        exclude_fields: list[str] | None = None,
    ) -> TaskState: ...
    def get_comment(self) -> str: ...
    def log_state_change_action(self, user: AbstractBaseUser | None, action: str) -> None: ...

    class Meta:
        verbose_name: _StrPromise
        verbose_name_plural: _StrPromise

# ---------------------------------------------------------------------------
# WorkflowMixin
# ---------------------------------------------------------------------------

class WorkflowMixin:
    @classmethod
    def check(cls, **kwargs: Any) -> list[CheckMessage]: ...
    @classmethod
    def get_default_workflow(cls) -> Workflow | None: ...
    @property
    def has_workflow(self) -> bool: ...
    def get_workflow(self) -> Workflow | None: ...
    @property
    def workflow_states(self) -> WorkflowStateQuerySet: ...
    @property
    def workflow_in_progress(self) -> bool: ...
    @property
    def current_workflow_state(self) -> WorkflowState | None: ...
    @property
    def current_workflow_task_state(self) -> TaskState | None: ...
    @property
    def current_workflow_task(self) -> Task | None: ...
    @property
    def status_string(self) -> _StrPromise: ...
    def get_lock(self) -> WorkflowLock | BaseLock | None: ...
