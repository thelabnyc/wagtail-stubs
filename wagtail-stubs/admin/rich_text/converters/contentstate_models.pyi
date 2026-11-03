from typing import Any

from draftjs_exporter import Block as _DraftBlock
from draftjs_exporter import ContentState as _DraftContentState
from draftjs_exporter import Entity as _DraftEntity
from draftjs_exporter import EntityRange as _DraftEntityRange
from draftjs_exporter import InlineStyleRange as _DraftInlineStyleRange

ALPHANUM: str

class Block:
    type: str
    depth: int
    text: str
    key: str
    inline_style_ranges: list[InlineStyleRange]
    entity_ranges: list[EntityRange]

    def __init__(self, typ: str, depth: int = 0, key: str | None = None) -> None: ...
    def as_dict(self) -> _DraftBlock: ...

class InlineStyleRange:
    style: str
    offset: int | None
    length: int | None

    def __init__(self, style: str) -> None: ...
    def as_dict(self) -> _DraftInlineStyleRange: ...

class Entity:
    entity_type: str
    mutability: str
    data: dict[str, Any]

    def __init__(self, entity_type: str, mutability: str, data: dict[str, Any]) -> None: ...
    def as_dict(self) -> _DraftEntity: ...

class EntityRange:
    key: int
    offset: int | None
    length: int | None

    def __init__(self, key: int) -> None: ...
    def as_dict(self) -> _DraftEntityRange: ...

class ContentState:
    blocks: list[Block]
    entity_count: int
    entity_map: dict[int, Entity]

    def __init__(self) -> None: ...
    def add_entity(self, entity: Entity) -> int: ...
    def as_dict(self) -> _DraftContentState: ...
    def as_json(self, **kwargs: Any) -> str: ...
