from django.utils.decorators import classonlymethod as classonlymethod
from django.views.generic import View
from django.db import models
from wagtail.images import get_image_model as get_image_model
from wagtail.images.exceptions import InvalidFilterSpecError as InvalidFilterSpecError
from wagtail.images.models import SourceImageIOError as SourceImageIOError
from wagtail.images.utils import generate_signature as generate_signature, verify_signature as verify_signature
from wagtail.utils.sendfile import sendfile as sendfile

def generate_image_url(image, filter_spec, viewname: str = 'wagtailimages_serve', key=None): ...

class ServeView(View):
    model: type[models.Model]
    action: str
    key: str | None
    @classonlymethod
    def as_view(cls, **initkwargs): ...
    def get(self, request, signature, image_id, filter_spec, filename=None): ...
    def serve(self, rendition): ...
    def redirect(self, rendition): ...

serve: View

class SendFileView(ServeView):
    backend: str | None
    def serve(self, rendition): ...
