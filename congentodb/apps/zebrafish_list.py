from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from congentodb.models import Zebrafish
from .zebrafish_viewer import ZebrafishViewer


class ZebrafishList(ModelAdminWidget):

    UID = "zebrafish"
    MODEL = Zebrafish

    TITLE = "Zebrafish"

    LIST_DISPLAY = [
        "line_name",
        "line_number",
        "line_type",
        "background",
        "genotype",
        "origin",
        "mta",
        "availability",
    ]

    LIST_FILTER = ["line_type", "mta", "availability"]

    SEARCH_FIELDS = [
        "line_name__icontains",
        "line_number__icontains",
        "line_type__icontains",
        "background__icontains",
        "genotype__icontains",
        "origin__icontains",
    ]

    EDITFORM_CLASS = ZebrafishViewer
    USE_DETAILS_TO_EDIT = False

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = "top"
    ORQUESTRA_MENU_ORDER = 4
    ORQUESTRA_MENU_ICON = "tint blue"

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
