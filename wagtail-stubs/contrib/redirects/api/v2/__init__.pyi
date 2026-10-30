from typing import Any

from django.db.models import QuerySet
from rest_framework import serializers
from rest_framework.filters import BaseFilterBackend
from rest_framework.request import Request
from wagtail.api.v2.filters import (
    FieldsFilter as FieldsFilter,
)
from wagtail.api.v2.filters import (
    OrderingFilter as OrderingFilter,
)
from wagtail.api.v2.filters import (
    SearchFilter as SearchFilter,
)
from wagtail.api.v2.serializers import BaseSerializer as BaseSerializer
from wagtail.api.v2.views import BaseAPIViewSet as BaseAPIViewSet
from wagtail.contrib.redirects.middleware import get_redirect as get_redirect
from wagtail.contrib.redirects.models import Redirect as Redirect

class RedirectSerializer(BaseSerializer):
    location: serializers.CharField

class RedirectsAPIViewSet(BaseAPIViewSet):
    base_serializer_class: type[RedirectSerializer]
    filter_backends: list[type[BaseFilterBackend]]
    body_fields: list[str]
    name: str
    model: type[Redirect]
    listing_default_fields: list[str]
    def find_object(self, queryset: QuerySet[Any], request: Request) -> Redirect | None: ...
