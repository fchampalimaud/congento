from pyforms_web.widgets.django.modelviewform import ModelViewFormWidget
from pyforms_web.organizers import segment
from ..models import Rodent
from confapp import conf


class RodentViewer(ModelViewFormWidget):

    MODEL = Rodent
    LAYOUT_POSITION = conf.ORQUESTRA_NEW_BIGWINDOW

    FIELDSETS = [
        'public',
        ("species", "strain_name", "common_name"),
        ("background", "background_other", " "),
        ("genotype", "genotype_other", " "),
        ("model_type", "model_type_other", " "),
        "origin",
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
