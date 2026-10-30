from dataclasses import dataclass
from typing import Literal

from bs4 import BeautifulSoup, Tag
from django.utils.functional import cached_property
from wagtail.admin.rich_text.converters.editor_html import DbWhitelister, EditorHTMLConverter

@dataclass
class RichTextRemoval:
    tag: str
    action: Literal["unwrapped", "removed"]
    reason: Literal["feature_disabled", "unknown_linktype", "unknown_embedtype", "missing_attribute"]
    attribute: str | None = None
    detail: str | None = None

class DbHtmlInputWhitelister(DbWhitelister):
    removals: list[RichTextRemoval]
    def clean(self, html: str) -> str: ...
    def clean_tag_node(self, doc: BeautifulSoup, tag: Tag) -> None: ...

class DbHTMLConverter(EditorHTMLConverter):
    @cached_property
    def whitelister(self) -> DbHtmlInputWhitelister: ...
    def clean(self, html: str) -> tuple[str, list[RichTextRemoval]]: ...
