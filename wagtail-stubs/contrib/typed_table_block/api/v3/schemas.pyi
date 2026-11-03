from typing import Any

from wagtail.api.v3.schemas.generators.blocks import BlockSchemaBuilder
from wagtail.blocks import Block

def typed_table_block_schema(builder: BlockSchemaBuilder, block: Block, name: str) -> Any: ...
