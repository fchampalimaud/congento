from django.apps import AppConfig


class CongentoDBConfig(AppConfig):
    name = "congentodb"
    verbose_name = "Congento DB"

    def ready(self):
        from .fly import FlyApp
        from .rodents_list import RodentsList
        from .fish_list import FishList

        global FlyApp
        global RodentsList
        global FishList
