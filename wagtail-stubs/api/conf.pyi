from typing import Any

from rest_framework.fields import Field

class APIField:
    name: str
    serializer: Field | None
    def __init__(self, name: str, serializer: Field | None = None) -> None: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
