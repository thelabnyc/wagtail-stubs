from django.contrib.auth.models import AbstractBaseUser, AnonymousUser
from ninja import UploadedFile
from pydantic import BaseModel
from wagtail.images.forms import BaseImageForm
from wagtail.images.models import AbstractImage

def build_image_form(
    model: type[AbstractImage],
    data: BaseModel,
    file: UploadedFile,
    user: AbstractBaseUser | AnonymousUser,
) -> BaseImageForm: ...
def build_image_update_form(
    instance: AbstractImage,
    data: BaseModel,
    user: AbstractBaseUser | AnonymousUser,
) -> BaseImageForm: ...
