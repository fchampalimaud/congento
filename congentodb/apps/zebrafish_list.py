from pyforms_web.widgets.django import ModelAdminWidget
from congentodb.models import Zebrafish
from .zebrafish_viewer import ZebrafishViewer
from confapp import conf

class ZebrafishList(ModelAdminWidget):

    UID = 'zebrafish-list'
    MODEL = Zebrafish
    TITLE = 'Zebrafish'

    EDITFORM_CLASS = ZebrafishViewer

    USE_DETAILS_TO_EDIT = False

    LIST_ROWS_PER_PAGE = 20

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'top'
    ORQUESTRA_MENU_ORDER = 1
    ORQUESTRA_MENU_ICON = 'tint blue'

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