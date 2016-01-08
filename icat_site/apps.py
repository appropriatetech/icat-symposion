from django.apps import AppConfig as BaseAppConfig
from django.utils.importlib import import_module


class AppConfig(BaseAppConfig):

    name = "icat_site"

    def ready(self):
        import_module("icat_site.receivers")
