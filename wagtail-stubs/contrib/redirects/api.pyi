from _typeshed import Incomplete
from wagtail.api.v2.filters import FieldsFilter as FieldsFilter, OrderingFilter as OrderingFilter, SearchFilter as SearchFilter
from wagtail.api.v2.serializers import BaseSerializer as BaseSerializer
from wagtail.api.v2.views import BaseAPIViewSet as BaseAPIViewSet
from wagtail.contrib.redirects.middleware import get_redirect as get_redirect
from wagtail.contrib.redirects.models import Redirect as Redirect

class RedirectSerializer(BaseSerializer):
    location: Incomplete

class RedirectsAPIViewSet(BaseAPIViewSet):
    base_serializer_class = RedirectSerializer
    filter_backends: Incomplete
    body_fields: Incomplete
    name: str
    model = Redirect
    listing_default_fields: Incomplete
    def find_object(self, queryset, request): ...
