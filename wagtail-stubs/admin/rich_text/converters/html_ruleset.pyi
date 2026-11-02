from collections.abc import Mapping
from typing import Any
import re

ELEMENT_SELECTOR: re.Pattern[str]
ELEMENT_WITH_ATTR_SELECTOR: re.Pattern[str]
ELEMENT_WITH_ATTR_EXACT_SINGLE_QUOTE_SELECTOR: re.Pattern[str]
ELEMENT_WITH_ATTR_EXACT_DOUBLE_QUOTE_SELECTOR: re.Pattern[str]
ELEMENT_WITH_ATTR_EXACT_UNQUOTED_SELECTOR: re.Pattern[str]

class HTMLRuleset:
    element_rules: dict[str, list[tuple[int, Any, Any]]]

    def __init__(self, rules: dict[str, Any] | list[tuple[str, Any]] | None = None) -> None: ...
    def add_rules(self, rules: Mapping[str, Any] | list[tuple[str, Any]]) -> None: ...
    def add_rule(self, selector: str, result: Any) -> None: ...
    def match(self, name: str, attrs: dict[str, str]) -> Any: ...
