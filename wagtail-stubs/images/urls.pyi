from django.urls import URLPattern, URLResolver
from wagtail.images.views.serve import serve as serve

urlpatterns: list[URLPattern | URLResolver]
