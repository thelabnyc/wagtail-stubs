from django.urls import URLPattern, URLResolver
from wagtail.documents.views import serve as serve

urlpatterns: list[URLPattern | URLResolver]
