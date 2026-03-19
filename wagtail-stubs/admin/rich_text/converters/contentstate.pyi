from draftjs_exporter.html import HTML as HTMLExporter
from wagtail.admin.rich_text.converters.html_to_contentstate import HtmlToContentStateHandler

class ContentstateConverter:
    features: list[str] | tuple[str, ...] | None
    html_to_contentstate_handler: HtmlToContentStateHandler
    exporter: HTMLExporter

    def __init__(self, features: list[str] | tuple[str, ...] | None = None) -> None: ...
    def from_database_format(self, html: str) -> str: ...
    def to_database_format(self, contentstate_json: str) -> str: ...
