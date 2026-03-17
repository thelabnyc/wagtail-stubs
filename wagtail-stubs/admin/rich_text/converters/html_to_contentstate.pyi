from html.parser import HTMLParser
from typing import Any

from wagtail.admin.rich_text.converters.contentstate_models import (
    Block,
    ContentState,
    Entity,
)
from wagtail.admin.rich_text.converters.html_ruleset import HTMLRuleset

STRIP_WHITESPACE: int
KEEP_WHITESPACE: int
FORCE_WHITESPACE: int

class HandlerState:
    current_block: Block | None
    current_inline_styles: list[Any]
    current_entity_ranges: list[Any]
    leading_whitespace: int
    list_depth: int
    list_item_type: str | None
    has_preceding_nonatomic_block: bool
    pushed_states: list[dict[str, Any]]

    def __init__(self) -> None: ...
    def push(self) -> None: ...
    def pop(self) -> None: ...

def add_paragraph_block(state: HandlerState, contentstate: ContentState) -> None: ...

class ListElementHandler:
    list_item_type: str
    def __init__(self, list_item_type: str) -> None: ...
    def handle_starttag(
        self, name: str, attrs: list[tuple[str, str | None]], state: HandlerState, contentstate: ContentState
    ) -> None: ...
    def handle_endtag(self, name: str, state: HandlerState, contentstate: ContentState) -> None: ...

class BlockElementHandler:
    block_type: str
    def __init__(self, block_type: str) -> None: ...
    def create_block(
        self, name: str, attrs: dict[str, str], state: HandlerState, contentstate: ContentState
    ) -> Block: ...
    def handle_starttag(
        self, name: str, attrs: list[tuple[str, str | None]], state: HandlerState, contentstate: ContentState
    ) -> None: ...
    def handle_endtag(self, name: str, state: HandlerState, contentstate: ContentState) -> None: ...

class ListItemElementHandler(BlockElementHandler):
    def __init__(self) -> None: ...
    def create_block(
        self, name: str, attrs: dict[str, str], state: HandlerState, contentstate: ContentState
    ) -> Block: ...

class InlineStyleElementHandler:
    style: str
    def __init__(self, style: str) -> None: ...
    def handle_starttag(
        self, name: str, attrs: list[tuple[str, str | None]], state: HandlerState, contentstate: ContentState
    ) -> None: ...
    def handle_endtag(self, name: str, state: HandlerState, contentstate: ContentState) -> None: ...

class InlineEntityElementHandler:
    entity_type: str
    mutability: str

    def __init__(self, entity_type: str) -> None: ...
    def handle_starttag(
        self, name: str, attrs: list[tuple[str, str | None]], state: HandlerState, contentstate: ContentState
    ) -> None: ...
    def get_attribute_data(self, attrs: dict[str, str]) -> dict[str, Any]: ...
    def handle_endtag(self, name: str, state: HandlerState, contentstate: ContentState) -> None: ...

class LinkElementHandler(InlineEntityElementHandler):
    mutability: str

class ExternalLinkElementHandler(LinkElementHandler):
    def get_attribute_data(self, attrs: dict[str, str]) -> dict[str, Any]: ...

class PageLinkElementHandler(LinkElementHandler):
    def get_attribute_data(self, attrs: dict[str, str]) -> dict[str, Any]: ...

class AtomicBlockEntityElementHandler:
    def handle_starttag(
        self, name: str, attrs: list[tuple[str, str | None]], state: HandlerState, contentstate: ContentState
    ) -> None: ...
    def handle_endtag(self, name: str, state: HandlerState, contentstate: ContentState) -> None: ...
    def create_entity(
        self, name: str, attrs: dict[str, str], state: HandlerState, contentstate: ContentState
    ) -> Entity: ...

class HorizontalRuleHandler(AtomicBlockEntityElementHandler):
    def create_entity(
        self, name: str, attrs: dict[str, str], state: HandlerState, contentstate: ContentState
    ) -> Entity: ...

class LineBreakHandler:
    def handle_starttag(
        self, name: str, attrs: list[tuple[str, str | None]], state: HandlerState, contentstate: ContentState
    ) -> None: ...
    def handle_endtag(self, name: str, state: HandlerState, contentstate: ContentState) -> None: ...

class HtmlToContentStateHandler(HTMLParser):
    paragraph_handler: BlockElementHandler
    element_handlers: HTMLRuleset
    state: HandlerState
    contentstate: ContentState
    open_elements: list[tuple[str, Any]]

    def __init__(self, features: tuple[str, ...] = ...) -> None: ...
    def reset(self) -> None: ...
    def handle_starttag(self, name: str, attrs: list[tuple[str, str | None]]) -> None: ...
    def handle_endtag(self, name: str) -> None: ...
    def handle_data(self, content: str) -> None: ...
    def close(self) -> None: ...
