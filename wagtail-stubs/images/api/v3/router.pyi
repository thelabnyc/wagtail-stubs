from typing import Any

from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import Router, Schema, Status, UploadedFile
from ninja.params.models import Body as _BodyParam
from ninja.params.models import File as _FileParam
from ninja.params.models import Form as _FormParam
from ninja.params.models import Query as _QueryParam
from pydantic import BaseModel
from wagtail.api.v3.pagination import WagtailLimitOffsetPagination
from wagtail.api.v3.registry import ContentTypeRegistration
from wagtail.api.v3.schemas.params import OrderingSchema, SearchSchema
from wagtail.images.api.v3.schemas import ImageSchema
from wagtail.images.models import AbstractImage

router: Router
Image: type[AbstractImage]
registered_schemas: ContentTypeRegistration

class ImageDetailSchema(ImageSchema): ...
class ImageCreateSchema(Schema): ...
class ImagePatchSchema(Schema): ...

BASE_IMAGE_READ_FIELDS: list[str]

def get_images_queryset(request: HttpRequest) -> QuerySet[AbstractImage]: ...
def list_images(
    request: HttpRequest,
    *,
    ordering: OrderingSchema | _QueryParam = ...,
    search: SearchSchema | _QueryParam = ...,
    ninja_pagination: WagtailLimitOffsetPagination.Input | None = None,
    **kwargs: Any,
) -> dict[str, Any]: ...
def get_image(request: HttpRequest, image_id: int) -> AbstractImage: ...
def create_image(
    request: HttpRequest, file: UploadedFile | _FileParam = ..., data: BaseModel | _FormParam = ...
) -> Status[AbstractImage]: ...
def update_image(request: HttpRequest, image_id: int, data: BaseModel | _BodyParam = ...) -> AbstractImage: ...
def delete_image(request: HttpRequest, image_id: int) -> Status[None]: ...
