from django.apps import AppConfig


class IzbaDocsApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "izba_docs_api"

    def ready(self):
        from . import signals
