from typing import Generic

from typing_extensions import TypeVar
from wagtail.admin.views.generic import lock as lock
from wagtail.models import AbstractPage

Page: type[AbstractPage]
_PageT = TypeVar("_PageT", bound=AbstractPage, default=AbstractPage)

class PageOperationViewMixin(Generic[_PageT]):
    model: type[_PageT]
    pk_url_kwarg: str
    def get_object(self) -> _PageT: ...
    def get_success_url(self): ...

class LockView(PageOperationViewMixin[_PageT], lock.LockView[_PageT]):
    def perform_operation(self): ...

class UnlockView(PageOperationViewMixin[_PageT], lock.UnlockView[_PageT]):
    def perform_operation(self): ...
    def get_success_message(self): ...
