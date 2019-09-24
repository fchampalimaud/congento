from confapp import conf
from pyforms_web.organizers import segment
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django import ModelFormWidget

from .. import models


# class MembershipInlineForm(ModelFormWidget):
#     FIELDSETS = [
#         segment(
#             ("email", "date_joined", "last_login"),
#             ("name", "display_name", "is_active"),
#         ),
#     ]

#     READ_ONLY = ["username", "email", "last_login", "date_joined"]

#     LAYOUT_POSITION = conf.ORQUESTRA_NEW_WINDOW

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)


class MembershipInline(ModelAdminWidget):
    MODEL = models.User

    LIST_DISPLAY = ["display_name", "email", "is_active"]
    LIST_HEADERS = ["Name", "Email", "Active"]

    # EDITFORM_CLASS = MembershipInlineForm

    USE_DETAILS_TO_ADD = False  # required to have form in NEW_TAB
    USE_DETAILS_TO_EDIT = False  # required to have form in NEW_TAB

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._list.item_selection_changed_event = lambda: None

    def has_add_permissions(self):
        return False


class InstitutionForm(ModelFormWidget):
    FIELDSETS = [
        ("name", [("acronym", "is_congento_member")]),
        segment("h3:Institution Members", "MembershipInline"),
    ]

    INLINES = [MembershipInline]

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.is_congento_member.checkbox_type = ""

    @property
    def title(self):
        try:
            return str(self.model_object)
        except AttributeError:
            pass  # apparently it defaults to App TITLE


class InstitutionsListApp(ModelAdminWidget):
    UID = "institutions"
    MODEL = models.Institution
    TITLE = "Institutions"

    LIST_DISPLAY = ["name", "acronym", "is_congento_member"]
    LIST_FILTER = ["is_congento_member"]
    SEARCH_FIELDS = ["name__icontains", "acronym__icontains"]

    EDITFORM_CLASS = InstitutionForm

    USE_DETAILS_TO_EDIT = False  # required to have form in NEW_TAB

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = "middle-left"
    ORQUESTRA_MENU_ORDER = 10
    ORQUESTRA_MENU_ICON = "building"

    @classmethod
    def has_permissions(cls, user):
        if user.is_superuser:
            return True
        return False
