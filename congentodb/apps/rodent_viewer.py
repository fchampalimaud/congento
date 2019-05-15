from pyforms_web.widgets.django.modelviewform import ModelViewFormWidget
from confapp import conf


class RodentViewer(ModelViewFormWidget):
    LAYOUT_POSITION = conf.ORQUESTRA_NEW_BIGWINDOW

    FIELDSETS = [
        ("species", "strain_name", "common_name"),
        ("background", "background_other", " "),
        ("genotype", "genotype_other", " "),
        ("model_type", "model_type_other", " "),
        "origin",
        ("availability", "mta"),
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
