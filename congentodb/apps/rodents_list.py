from pyforms_web.widgets.django import ModelAdminWidget
from congentodb.models import Rodent
from .rodent_viewer import RodentViewer
from confapp import conf

class RodentsList(ModelAdminWidget):
    UID = 'rodents-list'
    MODEL = Rodent

    TITLE = 'Rodents'

    EDITFORM_CLASS = RodentViewer

    USE_DETAILS_TO_EDIT = False

    LIST_ROWS_PER_PAGE = 20

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'top'
    ORQUESTRA_MENU_ORDER = 1
    ORQUESTRA_MENU_ICON = 'paw green'

    ########################################################

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