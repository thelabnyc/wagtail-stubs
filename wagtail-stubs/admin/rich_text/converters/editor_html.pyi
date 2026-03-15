from collections.abc import Callable
from typing import Protocol

from bs4 import Tag


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
