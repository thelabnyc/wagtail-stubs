import datetime
from collections.abc import Callable

from .exceptions import EmbedUnsupportedProviderException as EmbedUnsupportedProviderException
from .finders import get_finders as get_finders
from .models import Embed as Embed
from wagtail.coreutils import accepts_kwarg as accepts_kwarg, safe_md5 as safe_md5

_EmbedDict = dict[str, str | int | datetime.datetime | None]

def get_finder_for_embed(url: str, max_width: int | None = None, max_height: int | None = None) -> _EmbedDict: ...
def get_embed(url: str, max_width: int | None = None, max_height: int | None = None, finder: Callable[[str, int | None, int | None], _EmbedDict] = ...) -> Embed: ...
def get_embed_hash(url: str, max_width: int | None = None, max_height: int | None = None) -> str: ...
