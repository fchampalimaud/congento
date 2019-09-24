from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "users"

    def ready(self):
        from .. import signals  # noqa

        from .users import UsersListApp
        from .institutions import InstitutionsListApp

        global UsersListApp
        global InstitutionsListApp
