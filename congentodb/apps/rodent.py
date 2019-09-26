from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django.modelviewform import ModelViewFormWidget

from congentodb.models import Rodent

from .utils import ViewPermissionsMixin


class RodentViewer(ModelViewFormWidget):
    LAYOUT_POSITION = conf.ORQUESTRA_NEW_BIGWINDOW

    FIELDSETS = [
        ("species", "category", "strain_name", "common_name"),
        (
            "background",
            "zygosity",
            "coat_color",
            "reporter_gene",
            "inducible_cassette",
            "origin",
            "origin_other",
            "availability",
        ),
        "link",
        "line_description",
    ]

    @property
    def title(self):
        try:
            return "Rodent"
        except AttributeError:
            pass  # apparently it defaults to App TITLE


class RodentApp(ViewPermissionsMixin, ModelAdminWidget):

    UID = "rodent"
    MODEL = Rodent

    TITLE = "Rodent"

    LIST_DISPLAY = [
        "species",
        "strain_name",
        "common_name",
        "background",
        "origin",
        "availability",
    ]

    LIST_FILTER = [
        "species",
        "background",
        "category",
        "zygosity",
        "coat_color",
        "origin",
        "reporter_gene",
        "inducible_cassette",
        "availability",
        "congento_member__institution",
    ]

    SEARCH_FIELDS = [
        "strain_name__icontains",
        "common_name__icontains",
        "origin_other__icontains",
        "line_description__icontains",
    ]

    EDITFORM_CLASS = RodentViewer

    USE_DETAILS_TO_EDIT = False
    USE_DETAILS_TO_ADD = False

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = "top"
    ORQUESTRA_MENU_ORDER = 3
    ORQUESTRA_MENU_ICON = "large congento-rodent"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
