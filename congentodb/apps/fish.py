from confapp import conf
from pyforms_web.organizers import no_columns
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django.modelviewform import ModelViewFormWidget

from congentodb.models import Fish

from .utils import ViewPermissionsMixin


class FishViewer(ModelViewFormWidget):
    LAYOUT_POSITION = conf.ORQUESTRA_NEW_BIGWINDOW

    FIELDSETS = [
        ("species_name", "category_name", "strain_name", "common_name"),
        ("background", "genotype", "phenotype", "origin"),
        ("availability", "link"),
        no_columns("quarantine"),
        no_columns("mta"),
        "line_description",
    ]

    @property
    def title(self):
        try:
            return "Fish"
        except AttributeError:
            pass  # apparently it defaults to App TITLE


class FishApp(ViewPermissionsMixin, ModelAdminWidget):

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
        "congento_member__institution",
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
    USE_DETAILS_TO_ADD = False

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = "top"
    ORQUESTRA_MENU_ORDER = 4
    ORQUESTRA_MENU_ICON = "tint blue"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
