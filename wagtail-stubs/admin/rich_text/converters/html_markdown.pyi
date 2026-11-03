from collections.abc import Iterable
import re

from draftjs_exporter import HTMLExporter
from wagtail.admin.rich_text.converters.contentstate_models import ContentState, Entity
from wagtail.admin.rich_text.converters.editor_html import DbWhitelister
from wagtail.admin.rich_text.converters.html_to_contentstate import (
    AtomicBlockEntityElementHandler,
    HandlerState,
    HtmlToContentStateHandler,
)

INGEST_FEATURES: list[str]
DROP_ELEMENTS: set[str]
CONTAINER_ELEMENTS: set[str]
HEADING_ELEMENTS: set[str]
TEXT_BLOCK_ELEMENTS: set[str]
BLOCK_ELEMENTS: set[str]
INLINE_RENAMES: dict[str, str]
KNOWN_INLINE_ELEMENTS: set[str]
PERMALINK_TEXTS: set[str]
CODE_LANGUAGE_RE: re.Pattern[str]
LINE_START_ESCAPE_RE: re.Pattern[str]
MAX_COLSPAN: int
MAX_LIST_DEPTH: int
BLOCK_MARKER_ATTR: str
CODE_FENCE_RE: re.Pattern[str]

class ExternalImageElementHandler(AtomicBlockEntityElementHandler):
    def create_entity(
        self, name: str, attrs: dict[str, str], state: HandlerState, contentstate: ContentState
    ) -> Entity: ...

class IngestHtmlToContentStateHandler(HtmlToContentStateHandler):
    def __init__(self, features: Iterable[str] = ()) -> None: ...

class HTMLToMarkdownConverter:
    base_url: str | None
    content_selector: str | None
    tokens: list[str]
    token_prefix: str
    token_re: re.Pattern[str]
    whitelister: DbWhitelister
    exporter: HTMLExporter
    def __init__(self, *, base_url: str | None = None, content_selector: str | None = None) -> None: ...
    def convert(self, html: str) -> str: ...

def html_to_markdown(html: str, *, base_url: str | None = None, content_selector: str | None = None) -> str: ...
