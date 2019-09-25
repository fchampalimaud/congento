from django.apps import AppConfig


class CongentoDBConfig(AppConfig):
    name = "congentodb"
    verbose_name = "Congento DB"

    def ready(self):
        from .fly import FlyApp
        from .rodent import RodentApp
        from .fish import FishApp

        global FlyApp
        global RodentApp
        global FishApp
