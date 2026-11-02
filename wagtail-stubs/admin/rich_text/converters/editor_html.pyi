from collections.abc import Callable, Iterable, Sequence
from typing import Protocol

from bs4 import BeautifulSoup, Tag
from django.utils.functional import cached_property
from wagtail.models import AbstractPage
from wagtail.rich_text.rewriters import MultiRuleRewriter
from wagtail.whitelist import Whitelister

Page: type[AbstractPage]

class _EditorHTMLEmbedHandler(Protocol):
    @staticmethod
    def get_db_attributes(tag: Tag) -> dict[str, str]: ...
    @staticmethod
    def expand_db_attributes(attrs: dict[str, str]) -> str: ...

class _EditorHTMLLinkHandler(Protocol):
    @staticmethod
    def get_db_attributes(tag: Tag) -> dict[str, str]: ...
    @staticmethod
    def expand_db_attributes(attrs: dict[str, str]) -> str: ...

class WhitelistRule:
    element: str
    handler: Callable[[Tag], None]
    def __init__(self, element: str, handler: Callable[[Tag], None]) -> None: ...

class EmbedTypeRule:
    embed_type: str
    handler: _EditorHTMLEmbedHandler
    def __init__(self, embed_type: str, handler: _EditorHTMLEmbedHandler) -> None: ...

class LinkTypeRule:
    link_type: str
    handler: _EditorHTMLLinkHandler
    def __init__(self, link_type: str, handler: _EditorHTMLLinkHandler) -> None: ...

type _ConverterRule = WhitelistRule | EmbedTypeRule | LinkTypeRule

BASE_WHITELIST_RULES: dict[str, Callable[[Tag], None]]

class DbWhitelister(Whitelister):
    converter_rules: Sequence[_ConverterRule]
    def __init__(self, converter_rules: Sequence[_ConverterRule]) -> None: ...
    @cached_property
    def embed_handlers(self) -> dict[str, _EditorHTMLEmbedHandler]: ...
    @cached_property
    def link_handlers(self) -> dict[str, _EditorHTMLLinkHandler]: ...
    def clean_tag_node(self, doc: BeautifulSoup, tag: Tag) -> None: ...

class EditorHTMLConverter:
    converter_rules: list[_ConverterRule]
    def __init__(self, features: Iterable[str] | None = None) -> None: ...
    @cached_property
    def whitelister(self) -> DbWhitelister: ...
    def to_database_format(self, html: str) -> str: ...
    @cached_property
    def html_rewriter(self) -> MultiRuleRewriter: ...
    def from_database_format(self, html: str) -> str: ...

class PageLinkHandler:
    @staticmethod
    def get_db_attributes(tag: Tag) -> dict[str, str]: ...
    @staticmethod
    def expand_db_attributes(attrs: dict[str, str]) -> str: ...
