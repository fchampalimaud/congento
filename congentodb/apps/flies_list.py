from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from congentodb.models import Fly
from .fly_viewer import FlyViewer


class FliesList(ModelAdminWidget):

    UID = "flies"
    MODEL = Fly

    TITLE = "Flies"

    LIST_DISPLAY = ["specie", "genotype", "category"]

    LIST_FILTER = ["specie", "category"]

    SEARCH_FIELDS = [
        "genotype__icontains",
        "legacy1__icontains",
        "legacy2__icontains",
        "legacy3__icontains",
    ]

    EDITFORM_CLASS = FlyViewer
    USE_DETAILS_TO_EDIT = False

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = "top"
    ORQUESTRA_MENU_ORDER = 1
    ORQUESTRA_MENU_ICON = "bug red"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def has_add_permissions(self):
        return False

    def has_remove_permissions(self, obj):
        return False

    def has_view_permissions(self, obj):
        return True

    def has_update_permissions(self, obj):
        return False
