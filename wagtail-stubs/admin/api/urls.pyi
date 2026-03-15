from django.urls import URLPattern, URLResolver
from wagtail import hooks as hooks
from wagtail.api.v2.router import WagtailAPIRouter as WagtailAPIRouter

from .views import PagesAdminAPIViewSet as PagesAdminAPIViewSet

admin_api: WagtailAPIRouter
urlpatterns: list[URLPattern | URLResolver]
