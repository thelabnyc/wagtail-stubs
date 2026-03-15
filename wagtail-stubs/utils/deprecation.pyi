from types import ModuleType
from typing import Any

class RemovedInWagtail80Warning(DeprecationWarning): ...

removed_in_next_version_warning = RemovedInWagtail80Warning

class RemovedInWagtail90Warning(PendingDeprecationWarning): ...

class MovedDefinitionHandler:
    real_module: ModuleType
    moved_definitions: dict[str, str | tuple[str, str]]
    warning_class: type[Warning]
    def __init__(
        self, real_module: ModuleType, moved_definitions: dict[str, str | tuple[str, str]], warning_class: type[Warning]
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
