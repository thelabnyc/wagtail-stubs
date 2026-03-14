from _typeshed import Incomplete
from django.core.exceptions import PermissionDenied

class RevertToPageRevisionError(RuntimeError): ...
class RevertToPageRevisionPermissionError(PermissionDenied): ...

class RevertToPageRevisionAction:
    page: Incomplete
    revision: Incomplete
    user: Incomplete
    log_action: Incomplete
    approved_go_live_at: Incomplete
    changed: Incomplete
    clean: Incomplete
    def __init__(self, page, revision, user=None, log_action: str = 'wagtail.revert', approved_go_live_at=None, changed: bool = True, clean: bool = True) -> None: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def execute(self, skip_permission_checks: bool = False): ...
