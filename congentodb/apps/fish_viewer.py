from confapp import conf
from pyforms_web.organizers import no_columns
from pyforms_web.widgets.django.modelviewform import ModelViewFormWidget


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

    def has_add_permissions(self):
        return False

    def has_remove_permissions(self):
        return False

    def has_update_permissions(self):
        return False

    def has_view_permissions(self):
        return True
