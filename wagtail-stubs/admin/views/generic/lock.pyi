from django.db import models
from typing_extensions import TypeVar
from wagtail.admin.views.generic.base import BaseOperationView

_ModelT = TypeVar("_ModelT", bound=models.Model, default=models.Model)

class LockView(BaseOperationView[_ModelT]):
    success_message_extra_tags: str
    def perform_operation(self) -> None: ...

class UnlockView(BaseOperationView[_ModelT]):
    success_message_extra_tags: str
    def perform_operation(self) -> None: ...
    def get_success_message(self) -> str: ...
