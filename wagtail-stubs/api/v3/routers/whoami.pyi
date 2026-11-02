from typing import TypedDict

from django.http import HttpRequest
from ninja import Router, Schema

router: Router

class WhoAmIUserSchema(Schema):
    id: str
    username: str
    email: str
    first_name: str
    last_name: str
    is_superuser: bool

class WhoAmIProfileSchema(Schema):
    avatar_url: str | None

class WhoAmISchema(Schema):
    user: WhoAmIUserSchema
    profile: WhoAmIProfileSchema
    groups: list[str]

class _WhoAmIUser(TypedDict):
    id: str
    username: str
    email: str
    first_name: str
    last_name: str
    is_superuser: bool

class _WhoAmIProfile(TypedDict):
    avatar_url: str | None

class _WhoAmI(TypedDict):
    user: _WhoAmIUser
    profile: _WhoAmIProfile
    groups: list[str]

def whoami(request: HttpRequest) -> _WhoAmI: ...
