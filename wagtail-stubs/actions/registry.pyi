from typing import Any

from django.db.models import Model
from wagtail.actions.base import BaseAction

class ActionRegistry:
    actions: dict[type[Model], dict[str, type[BaseAction[Any]]]]
    has_scanned_for_actions: bool
    def __init__(self) -> None: ...
    def register[A: type[BaseAction[Any]]](self, model: type[Model], action_class: A) -> A: ...
    def get_actions_for_model(self, model: type[Model]) -> dict[str, type[BaseAction[Any]]]: ...
    def get_action_class(self, model: type[Model], action_name: str) -> type[BaseAction[Any]] | None: ...

action_registry: ActionRegistry
