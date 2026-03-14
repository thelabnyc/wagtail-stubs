from _typeshed import Incomplete
from django.core.exceptions import PermissionDenied
from wagtail.log_actions import log as log
from wagtail.signals import unpublished as unpublished

logger: Incomplete

class UnpublishPermissionError(PermissionDenied): ...

class UnpublishAction:
    object: Incomplete
    set_expired: Incomplete
    commit: Incomplete
    user: Incomplete
    log_action: Incomplete
    def __init__(self, object, set_expired: bool = False, commit: bool = True, user=None, log_action: bool = True) -> None: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> None: ...
