from _typeshed import Incomplete
from wagtail import hooks as hooks
from wagtail.admin.views.bulk_action import BulkAction as BulkAction

class BulkActionRegistry:
    actions: Incomplete
    has_scanned_for_bulk_actions: bool
    def __init__(self) -> None: ...
    def get_bulk_actions_for_model(self, app_label, model_name): ...
    def get_bulk_action_class(self, app_label, model_name, action_type): ...

bulk_action_registry: Incomplete
