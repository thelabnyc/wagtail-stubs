from django.urls import URLPattern, URLResolver
from wagtail.images.views import images as images, multiple as multiple

app_name: str
urlpatterns: list[URLPattern | URLResolver]
