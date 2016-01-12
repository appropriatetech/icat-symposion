from django.apps import AppConfig as BaseAppConfig
from importlib import import_module


class AppConfig(BaseAppConfig):

    name = "icat_site"

    def ready(self):
        import_module("icat_site.receivers")
