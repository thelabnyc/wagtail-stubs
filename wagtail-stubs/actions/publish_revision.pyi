from _typeshed import Incomplete
from django.core.exceptions import PermissionDenied
from wagtail.log_actions import log as log
from wagtail.models import Revision as Revision
from wagtail.permission_policies.base import ModelPermissionPolicy as ModelPermissionPolicy
from wagtail.signals import published as published
from wagtail.utils.timestamps import ensure_utc as ensure_utc

logger: Incomplete

class PublishPermissionError(PermissionDenied): ...

class PublishRevisionAction:
    revision: Incomplete
    object: Incomplete
    permission_policy: Incomplete
    user: Incomplete
    changed: Incomplete
    log_action: Incomplete
    previous_revision: Incomplete
    def __init__(self, revision: Revision, user=None, changed: bool = True, log_action: bool = True, previous_revision: Revision | None = None) -> None: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def log_scheduling_action(self) -> None: ...
    def execute(self, skip_permission_checks: bool = False): ...
