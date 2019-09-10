from django.apps import AppConfig


class CongentoConfig(AppConfig):
    name = "congento"

    def ready(self):

        # from .flies_list import FliesList
        # from .rodents_list import RodentsList
        from .fish import FishApp

        # global FliesList
        # global RodentsList
        global FishApp

        pass
