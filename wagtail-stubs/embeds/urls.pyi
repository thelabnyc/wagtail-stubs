from django.urls import URLPattern, URLResolver
from wagtail.embeds.views import chooser as chooser

app_name: str
urlpatterns: list[URLPattern | URLResolver]
