from collections.abc import Iterable

from wagtail.images.models import AbstractImage, AbstractRendition, Filter

def get_rendition_or_not_found(image: AbstractImage, specs: Filter | str) -> AbstractRendition: ...
def get_renditions_or_not_found(
    image: AbstractImage, specs: Iterable[Filter | str]
) -> dict[str, AbstractRendition]: ...
