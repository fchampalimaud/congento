from confapp import conf
from pyforms_web.organizers import segment
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django.modelviewform import ModelViewFormWidget

from congentodb.models import Fly

from .utils import ViewPermissionsMixin


class FlyViewer(ModelViewFormWidget):
    LAYOUT_POSITION = conf.ORQUESTRA_NEW_BIGWINDOW

    FIELDSETS = [
        'institution',
        segment(
            'specie',
            ('legacy1', 'legacy2', 'legacy3'),
            'category'
        ),
        'h3:Genotype',
        segment(
            'genotype',
            ('chrx', 'chry', 'bal1'),
            ('chr2', 'bal2'),
            ('chr3', 'bal3'),
            'chr4',
            'chru'
        ),
        'h3:More',
        segment('flydbid'),
    ]


class FlyApp(ViewPermissionsMixin, ModelAdminWidget):

    UID = "fly"
    MODEL = Fly

    TITLE = "Fly"

    LIST_DISPLAY = ["species", "genotype", "categories", "origin", "institution_name"
]

    LIST_FILTER = ["species", "origin_center", "categories"]

    SEARCH_FIELDS = [
        "genotype__icontains",
    ]

    EDITFORM_CLASS = FlyViewer

    USE_DETAILS_TO_EDIT = False
    USE_DETAILS_TO_ADD = False

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = "top"
    ORQUESTRA_MENU_ORDER = 2
    ORQUESTRA_MENU_ICON = "bug red"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
