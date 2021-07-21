from django.apps import AppConfig


class IzbaDocsApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "izba_docs_api"
    verbose_name = "Izba Docs API"

    def ready(self):
        from . import signals
