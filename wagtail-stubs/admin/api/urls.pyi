from django.urls import URLPattern, URLResolver

from .v3.api import api as api

urlpatterns: list[URLPattern | URLResolver]
