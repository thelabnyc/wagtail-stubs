from wagtail.admin.mail import (
    GroupApprovalTaskStateSubmissionEmailNotifier as GroupApprovalTaskStateSubmissionEmailNotifier,
)
from wagtail.admin.mail import (
    WorkflowStateApprovalEmailNotifier as WorkflowStateApprovalEmailNotifier,
)
from wagtail.admin.mail import (
    WorkflowStateRejectionEmailNotifier as WorkflowStateRejectionEmailNotifier,
)
from wagtail.admin.mail import (
    WorkflowStateSubmissionEmailNotifier as WorkflowStateSubmissionEmailNotifier,
)
from wagtail.models import TaskState as TaskState
from wagtail.models import WorkflowState as WorkflowState
from wagtail.signals import (
    task_submitted as task_submitted,
)
from wagtail.signals import (
    workflow_approved as workflow_approved,
)
from wagtail.signals import (
    workflow_rejected as workflow_rejected,
)
from wagtail.signals import (
    workflow_submitted as workflow_submitted,
)

task_submission_email_notifier: GroupApprovalTaskStateSubmissionEmailNotifier
workflow_submission_email_notifier: WorkflowStateSubmissionEmailNotifier
workflow_approval_email_notifier: WorkflowStateApprovalEmailNotifier
workflow_rejection_email_notifier: WorkflowStateRejectionEmailNotifier

def register_signal_handlers() -> None: ...
