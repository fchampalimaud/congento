from django.apps import AppConfig


class CongentoDBConfig(AppConfig):
    name = "congentodb"
    verbose_name = "Congento DB"

    def ready(self):
        from .flies_list import FliesList
        from .rodents_list import RodentsList
        from .zebrafish_list import ZebrafishList

        global FliesList
        global RodentsList
        global ZebrafishList
