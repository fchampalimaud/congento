from pyforms_web.widgets.django.modelviewform import ModelViewFormWidget
from pyforms_web.organizers import segment
from ..models import Zebrafish
from confapp import conf


class ZebrafishViewer(ModelViewFormWidget):

    MODEL = Zebrafish
    LAYOUT_POSITION = conf.ORQUESTRA_NEW_BIGWINDOW

    FIELDSETS = [
        'public',
        ("line_name", "line_number", "line_type", "line_type_other"),
        ("background", "genotype", "phenotype", "origin"),
        ("availability", "mta", 'lab'),
        "link",
        "comments"
    ]

    def has_add_permissions(self):
        return False

    def has_remove_permissions(self):
        return False

    def has_update_permissions(self):
        return False

    def has_view_permissions(self):
        return True
