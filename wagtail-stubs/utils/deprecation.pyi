from types import ModuleType
from typing import Any

class RemovedInWagtail90Warning(DeprecationWarning): ...

removed_in_next_version_warning = RemovedInWagtail90Warning

class RemovedInWagtail100Warning(PendingDeprecationWarning): ...

class MovedDefinitionHandler:
    real_module: ModuleType
    moved_definitions: dict[str, str | tuple[str, str]]
    warning_class: type[Warning]
    def __init__(
        self, real_module: ModuleType, moved_definitions: dict[str, str | tuple[str, str]], warning_class: type[Warning]
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
