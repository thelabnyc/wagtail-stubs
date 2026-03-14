from wagtail.admin.views.generic.base import BaseOperationView

class LockView(BaseOperationView):
    success_message_extra_tags: str
    def perform_operation(self) -> None: ...

class UnlockView(BaseOperationView):
    success_message_extra_tags: str
    def perform_operation(self) -> None: ...
    def get_success_message(self) -> str: ...
