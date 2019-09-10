from confapp import conf

from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django import ModelViewFormWidget

from congento.models import Fish


class FishForm(ModelViewFormWidget):

    FIELDSETS = [
        ("line_name", "line_number", "line_type", "line_type_other"),
        ("background", "genotype", "phenotype", "origin"),
        ("availability", "mta"),
        "link",
        "comments",
    ]

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_BIGWINDOW

    def has_add_permissions(self):
        return False

    def has_remove_permissions(self):
        return False

    def has_update_permissions(self):
        return False

    def has_view_permissions(self):
        return True


class FishApp(ModelAdminWidget):

    UID = "fish"
    MODEL = Fish

    TITLE = "Fish"

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

    EDITFORM_CLASS = FishForm
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
