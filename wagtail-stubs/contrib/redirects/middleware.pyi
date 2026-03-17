from django.utils.deprecation import MiddlewareMixin
from wagtail.contrib.redirects import models as models
from wagtail.models.sites import Site as Site

def get_redirect(request, encoded_path): ...

class RedirectMiddleware(MiddlewareMixin):
    def process_response(self, request, response): ...
