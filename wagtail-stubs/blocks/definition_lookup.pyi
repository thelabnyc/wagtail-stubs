from collections import defaultdict
from typing import Any

from wagtail.blocks.base import Block

class BlockDefinitionLookup:
    blocks: dict[int, tuple[str, list[Any], dict[str, Any]]]
    block_classes: dict[str, type[Any]]
    def __init__(
        self, blocks: dict[int, tuple[str, list[Any], dict[str, Any]]]
    ) -> None: ...
    def get_block(self, index: int) -> Block: ...

class BlockDefinitionLookupBuilder:
    blocks: list[tuple[str, Any, Any]]
    block_indexes_by_type: defaultdict[str, list[tuple[int, tuple[str, Any, Any]]]]
    def __init__(self) -> None: ...
    def add_block(self, block: Block) -> int: ...
    def get_lookup_as_dict(self) -> dict[int, tuple[str, Any, Any]]: ...
