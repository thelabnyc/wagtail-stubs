from django.urls import URLPattern, URLResolver
from wagtail.images.views import images as images
from wagtail.images.views import multiple as multiple

app_name: str
urlpatterns: list[URLPattern | URLResolver]
