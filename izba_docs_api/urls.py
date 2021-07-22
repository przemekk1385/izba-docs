from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.urls import re_path

from . import views
from .apps import IzbaDocsApiConfig

app_name = IzbaDocsApiConfig.name
urlpatterns = [
    re_path(r"^docs/(?P<path>.*)$", views.serve_document, name="serve_file"),
]
