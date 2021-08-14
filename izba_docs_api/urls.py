from django.urls import include, re_path

from . import views
from .apps import IzbaDocsApiConfig
from .routers import router

API_VERSION_PREFIX = "api/v1/"

app_name = IzbaDocsApiConfig.name
urlpatterns = [
    re_path(f"^{API_VERSION_PREFIX}", include(router.urls)),
    re_path(r"^docs/(?P<path>.*)$", views.document_serve, name="document-serve"),
]
