from _typeshed import Incomplete
from django.core.exceptions import PermissionDenied
from wagtail.log_actions import log as log
from wagtail.signals import post_page_move as post_page_move, pre_page_move as pre_page_move

logger: Incomplete

class MovePagePermissionError(PermissionDenied): ...

class MovePageAction:
    page: Incomplete
    target: Incomplete
    pos: Incomplete
    user: Incomplete
    def __init__(self, page, target, pos=None, user=None) -> None: ...
    def check(self, parent_after, skip_permission_checks: bool = False) -> None: ...
    def execute(self, skip_permission_checks: bool = False): ...
