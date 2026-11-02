from collections.abc import Callable
from typing import Any, ClassVar, Literal, TypeAlias, overload

from wagtail.admin.rich_text.converters.db_html import RichTextRemoval

RichTextOutputFormat: TypeAlias = Literal["db_html", "html", "db_markdown", "markdown"]  # NOQA:UP040
RichTextInputFormat: TypeAlias = Literal["db_html", "db_markdown"]  # NOQA:UP040

class RichTextFormatError(ValueError): ...

class APIRichText:
    FORMAT_DB_HTML: ClassVar[Literal["db_html"]]
    FORMAT_HTML: ClassVar[Literal["html"]]
    FORMAT_DB_MARKDOWN: ClassVar[Literal["db_markdown"]]
    FORMAT_MARKDOWN: ClassVar[Literal["markdown"]]
    DEFAULT_FORMAT: ClassVar[RichTextOutputFormat]
    SETTING_NAME: ClassVar[str]
    @classmethod
    def check_setting(cls) -> None: ...
    @classmethod
    def get_default_format(cls) -> RichTextOutputFormat: ...
    @classmethod
    def resolve_format(cls, rich_text_format: str | None = None) -> RichTextOutputFormat: ...
    @overload
    @classmethod
    def serialize(cls, value: None, *, format: RichTextOutputFormat, features: list[str] | None = None) -> None: ...
    @overload
    @classmethod
    def serialize(cls, value: str, *, format: RichTextOutputFormat, features: list[str] | None = None) -> Any: ...
    @classmethod
    def parse_input(cls, value: str | dict[str, Any]) -> tuple[RichTextInputFormat, str]: ...
    @classmethod
    def sanitize_db_html(
        cls, content: str, *, features: list[str] | None = None
    ) -> tuple[str, list[RichTextRemoval]]: ...
    @staticmethod
    def convert_db_markdown_input(
        content: str, *, features: list[str] | None = None
    ) -> tuple[str, list[RichTextRemoval]]: ...
    @classmethod
    def convert_input(
        cls, value: str | dict[str, Any], *, features: list[str] | None = None
    ) -> tuple[str, list[RichTextRemoval]]: ...
    @classmethod
    def _input_converters(cls) -> dict[RichTextInputFormat, Callable[..., tuple[str, list[RichTextRemoval]]]]: ...
    @classmethod
    def _serializers(cls) -> dict[RichTextOutputFormat, Callable[..., Any]]: ...
    @staticmethod
    def _serialize_db_html(value: str, *, features: list[str] | None = None) -> str: ...
    @staticmethod
    def _serialize_html(value: str, *, features: list[str] | None = None) -> str: ...
    @staticmethod
    def _serialize_db_markdown(value: str, *, features: list[str] | None = None) -> str: ...
    @staticmethod
    def _serialize_markdown(value: str, *, features: list[str] | None = None) -> str: ...
    @classmethod
    def _validate_format(cls, rich_text_format: str) -> None: ...
