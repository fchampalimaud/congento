from pyforms_web.widgets.django import ModelAdminWidget
from congentodb.models import Zebrafish
from confapp import conf

class ZebrafishList(ModelAdminWidget):

    UID = 'zebrafish-list'
    MODEL = Zebrafish
    TITLE = 'Zebrafish'

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'left'
    ORQUESTRA_MENU_ORDER = 1
    ORQUESTRA_MENU_ICON = 'bug'
    ########################################################

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
