from _typeshed import Incomplete

class MenuItem:
    label: Incomplete
    url: Incomplete
    icon_name: Incomplete
    priority: Incomplete
    def __init__(self, label: str, url: str, icon_name: str = '', priority: int = 1000) -> None: ...
    def is_shown(self, user): ...
    def __lt__(self, other): ...
