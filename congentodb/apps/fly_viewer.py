from pyforms_web.widgets.django.modelviewform import ModelViewFormWidget
from pyforms_web.organizers import segment
from ..models import Fly
from confapp import conf


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
        segment(
            ('hospital', 'died'),
        ),
        'h3:More',
        segment('flydbid'),
    ]

    def has_add_permissions(self):
        return False

    def has_remove_permissions(self):
        return False

    def has_update_permissions(self):
        return False

    def has_view_permissions(self):
        return True
