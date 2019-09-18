from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from congentodb.models import Fish
from .fish_viewer import FishViewer


class FishList(ModelAdminWidget):

    UID = "fish"
    MODEL = Fish

    TITLE = "Fish"

    LIST_DISPLAY = [
        "species_name",
        "category_name",
        "strain_name",
        "genotype",
        "background",
        "origin",
        "mta",
        "availability",
    ]

    LIST_FILTER = [
        "species_name",
        "category_name",
        "quarantine",
        # "location",
        "mta",
        "availability",
    ]

    SEARCH_FIELDS = [
        "strain_name__icontains",
        "common_name__icontains",
        "background__icontains",
        "genotype__icontains",
        "phenotype__icontains",
        "origin__icontains",
        "line_description__icontains",
    ]

    EDITFORM_CLASS = FishViewer
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
