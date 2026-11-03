from wagtail.actions.base import BaseAction as BaseAction
from wagtail.actions.convert_alias import ConvertAliasPageAction as ConvertAliasPageAction
from wagtail.actions.copy_for_translation import CopyForTranslationAction as CopyForTranslationAction
from wagtail.actions.copy_for_translation import CopyPageForTranslationAction as CopyPageForTranslationAction
from wagtail.actions.copy_page import CopyPageAction as CopyPageAction
from wagtail.actions.create import CreateAction as CreateAction
from wagtail.actions.create import CreatePermissionError as CreatePermissionError
from wagtail.actions.create_alias import CreatePageAliasAction as CreatePageAliasAction
from wagtail.actions.create_page import CreatePageAction as CreatePageAction
from wagtail.actions.delete import DeleteAction as DeleteAction
from wagtail.actions.delete import DeletePermissionError as DeletePermissionError
from wagtail.actions.delete_page import DeletePageAction as DeletePageAction
from wagtail.actions.edit import EditAction as EditAction
from wagtail.actions.edit import EditPermissionError as EditPermissionError
from wagtail.actions.edit_page import EditPageAction as EditPageAction
from wagtail.actions.move_page import MovePageAction as MovePageAction
from wagtail.actions.publish_page_revision import PublishPageRevisionAction as PublishPageRevisionAction
from wagtail.actions.publish_revision import PublishRevisionAction as PublishRevisionAction
from wagtail.actions.registry import ActionRegistry as ActionRegistry
from wagtail.actions.registry import action_registry as action_registry
from wagtail.actions.revert_to_page_revision import RevertToPageRevisionAction as RevertToPageRevisionAction
from wagtail.actions.revert_to_revision import RevertToRevisionAction as RevertToRevisionAction
from wagtail.actions.unpublish import UnpublishAction as UnpublishAction
from wagtail.actions.unpublish_page import UnpublishPageAction as UnpublishPageAction
from wagtail.actions.workflow import ApproveTaskStateAction as ApproveTaskStateAction
from wagtail.actions.workflow import CancelWorkflowAction as CancelWorkflowAction
from wagtail.actions.workflow import RejectTaskStateAction as RejectTaskStateAction
from wagtail.actions.workflow import ResumeWorkflowAction as ResumeWorkflowAction
from wagtail.actions.workflow import SubmitWorkflowAction as SubmitWorkflowAction
from wagtail.actions.workflow import WorkflowAction as WorkflowAction
from wagtail.actions.workflow import WorkflowStateError as WorkflowStateError
from wagtail.actions.workflow import can_edit_instance as can_edit_instance
from wagtail.actions.workflow import get_available_workflow_transitions as get_available_workflow_transitions

__all__ = [
    "BaseAction",
    "ApproveTaskStateAction",
    "CancelWorkflowAction",
    "ConvertAliasPageAction",
    "CopyForTranslationAction",
    "CopyPageAction",
    "CopyPageForTranslationAction",
    "CreateAction",
    "CreatePageAction",
    "CreatePageAliasAction",
    "CreatePermissionError",
    "DeletePageAction",
    "EditAction",
    "EditPageAction",
    "EditPermissionError",
    "DeleteAction",
    "DeletePermissionError",
    "MovePageAction",
    "PublishRevisionAction",
    "PublishPageRevisionAction",
    "RevertToPageRevisionAction",
    "RevertToRevisionAction",
    "RejectTaskStateAction",
    "ResumeWorkflowAction",
    "SubmitWorkflowAction",
    "UnpublishAction",
    "UnpublishPageAction",
    "WorkflowAction",
    "WorkflowStateError",
    "can_edit_instance",
    "get_available_workflow_transitions",
    "ActionRegistry",
    "action_registry",
]

def register_default_actions() -> None: ...
