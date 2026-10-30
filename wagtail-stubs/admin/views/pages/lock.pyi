from wagtail.admin.views.generic import lock as lock
from wagtail.models import AbstractPage

Page: type[AbstractPage]

class PageOperationViewMixin:
    model: type[AbstractPage]
    pk_url_kwarg: str
    def get_object(self): ...
    def get_success_url(self): ...

class LockView(PageOperationViewMixin, lock.LockView):
    def perform_operation(self): ...

class UnlockView(PageOperationViewMixin, lock.UnlockView):
    def perform_operation(self): ...
    def get_success_message(self): ...
