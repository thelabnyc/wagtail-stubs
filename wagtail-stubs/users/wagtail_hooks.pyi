from wagtail import hooks as hooks
from wagtail.users.views.bulk_actions import (
    AssignRoleBulkAction as AssignRoleBulkAction,
)
from wagtail.users.views.bulk_actions import (
    DeleteBulkAction as DeleteBulkAction,
)
from wagtail.users.views.bulk_actions import (
    SetActiveStateBulkAction as SetActiveStateBulkAction,
)

def get_viewset_cls(app_config, viewset_name): ...
def register_viewset(): ...
