from collections.abc import Callable, Iterable
from typing import Protocol

from django.db.models import Model
from django.http import HttpRequest

class _PermissionDecorator(Protocol):
    def __call__[**P, R](self, view_func: Callable[P, R], /) -> Callable[P, R]: ...

def require_any_permission(
    model: type[Model] | Callable[..., type[Model]],
    actions: Iterable[str] = ("add", "change", "delete", "view"),
) -> _PermissionDecorator: ...
def get_restricted_collection_ids(request: HttpRequest) -> set[int]: ...
