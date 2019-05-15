from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from congentodb.models import Rodent
from .rodent_viewer import RodentViewer


class RodentsList(ModelAdminWidget):

    UID = "rodents"
    MODEL = Rodent

    TITLE = "Rodents"

    LIST_DISPLAY = [
        "species",
        "strain_name",
        "common_name",
        "background",
        "genotype",
        "model_type",
        "origin",
        "mta",
        "availability",
    ]

    LIST_FILTER = [
        "species",
        "background",
        "genotype",
        "model_type",
        "mta",
        "availability",
    ]

    SEARCH_FIELDS = [
        "species__icontains",
        "strain_name__icontains",
        "common_name__icontains",
        "background__icontains",
        "genotype__icontains",
        "model_type__icontains",
        "origin__icontains",
    ]

    EDITFORM_CLASS = RodentViewer
    USE_DETAILS_TO_EDIT = False

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = "top"
    ORQUESTRA_MENU_ORDER = 1
    ORQUESTRA_MENU_ICON = "paw green"

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
