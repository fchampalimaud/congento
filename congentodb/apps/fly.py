from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django.modelviewform import ModelViewFormWidget

from congentodb.models import Fly

from .utils import ViewPermissionsMixin


class FlyViewer(ModelViewFormWidget):
    LAYOUT_POSITION = conf.ORQUESTRA_NEW_BIGWINDOW

    FIELDSETS = [
        ("species", "origin", "origin_center", "get_institution_name"),
        "genotype",
        ("categories", "special_husbandry_conditions", "line_description"),
    ]

    @property
    def title(self):
        try:
            return "Fly Stock"
            # return self.model_object.species
        except AttributeError:
            pass  # apparently it defaults to App TITLE


class FlyApp(ViewPermissionsMixin, ModelAdminWidget):

    UID = "fly"
    MODEL = Fly

    TITLE = "Fly"

    LIST_DISPLAY = ["species", "genotype", "origin", "origin_center", "get_institution_name"]

    LIST_FILTER = ["species", "origin", "origin_center", "congento_member__institution"]

    SEARCH_FIELDS = [
        "genotype__icontains",
        "categories__icontains",
        "special_husbandry_conditions__icontains",
        "line_description__icontains",
    ]

    EDITFORM_CLASS = FlyViewer

    USE_DETAILS_TO_EDIT = False
    USE_DETAILS_TO_ADD = False

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = "top"
    ORQUESTRA_MENU_ORDER = 2
    ORQUESTRA_MENU_ICON = "large congento-fly"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
