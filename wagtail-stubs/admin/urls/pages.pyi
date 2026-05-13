from django.urls import URLPattern, URLResolver
from wagtail.admin.viewsets.pages import PageViewSetRegistry

app_name: str
urlpatterns: list[URLPattern | URLResolver]

page_viewset_registry: PageViewSetRegistry
