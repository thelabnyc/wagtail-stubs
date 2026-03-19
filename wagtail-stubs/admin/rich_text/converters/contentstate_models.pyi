from typing import Any

class Block:
    type: str
    depth: int
    text: str
    key: str
    inline_style_ranges: list[InlineStyleRange]
    entity_ranges: list[EntityRange]

    def __init__(self, typ: str, depth: int = 0, key: str | None = None) -> None: ...
    def as_dict(self) -> dict[str, Any]: ...

class InlineStyleRange:
    style: str
    offset: int | None
    length: int | None

    def __init__(self, style: str) -> None: ...
    def as_dict(self) -> dict[str, Any]: ...

class Entity:
    entity_type: str
    mutability: str
    data: dict[str, Any]

    def __init__(self, entity_type: str, mutability: str, data: dict[str, Any]) -> None: ...
    def as_dict(self) -> dict[str, Any]: ...

class EntityRange:
    key: int
    offset: int | None
    length: int | None

    def __init__(self, key: int) -> None: ...
    def as_dict(self) -> dict[str, Any]: ...

class ContentState:
    blocks: list[Block]
    entity_count: int
    entity_map: dict[int, Entity]

    def __init__(self) -> None: ...
    def add_entity(self, entity: Entity) -> int: ...
    def as_dict(self) -> dict[str, Any]: ...
    def as_json(self, **kwargs: Any) -> str: ...
