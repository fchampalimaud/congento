from django.apps import AppConfig


class CongentoConfig(AppConfig):
    name = "congento"

    def ready(self):
        from .fish import FishApp

        global FishApp
