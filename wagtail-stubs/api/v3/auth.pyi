from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest
from ninja.security import HttpBearer
from ninja.security.http import HttpAuthBase
from wagtail.models import APIToken

class BearerTokenAuth(HttpBearer):
    def authenticate(self, request: HttpRequest, token: str) -> APIToken | None: ...
    def _touch_last_used(self, api_token: APIToken) -> None: ...

class AllowAnonymous(HttpAuthBase):
    def __call__(self, request: HttpRequest) -> AnonymousUser: ...
