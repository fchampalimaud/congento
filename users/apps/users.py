from confapp import conf
from django.contrib.auth import get_user_model
from pyforms_web.organizers import segment
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django import ModelFormWidget

from pyforms.controls import ControlButton

from .. import models

User = get_user_model()


class UserForm(ModelFormWidget):
    MODEL = User

    FIELDSETS = [
        segment(
            ("email", "date_joined", "last_login"),
            ("name", "display_name", "is_active"),
        ),
        segment(
            "info:Select an Institution from the list or create a new one.",
            ("institution", "institution_to_validate", "_btn_new_institution"),
        ),
    ]

    READ_ONLY = ["username", "email", "last_login", "date_joined"]

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._btn_new_institution = ControlButton(
            label='<i class="building icon"></i>Add Institution',
            css="fluid green",
            default=self.__create_new_institution,
        )

        self.is_active.checkbox_type = ""

        # Custom labels because Django likes smallcase verbose names
        self.email.label = "Email address"
        self.date_joined.label = "Date joined"
        self.last_login.label = "Last login"
        self.is_active.label = "Active"

    def __create_new_institution(self):
        new_institution_name = self.institution_to_validate.value

        if not new_institution_name:
            self.alert("Institution name not provided.")
            return

        if len(new_institution_name) < 5:
            self.alert("Institution name is too short.")
            return

        institution, created = models.Institution.objects.get_or_create(
            name=new_institution_name
        )

        if created:
            self.success("New institution created: %s" % institution)

        self.institution.value = institution.pk
        self.institution_to_validate.value = ""

    @property
    def title(self):
        try:
            return self.model_object.get_display_name()
        except AttributeError:
            pass  # apparently it defaults to App TITLE


class UsersListApp(ModelAdminWidget):

    UID = "users"
    MODEL = models.User
    TITLE = "Users"

    LIST_DISPLAY = [
        "get_display_name",
        "email",
        "institution",
        "is_active",
        "date_joined",
        "last_login",
    ]

    LIST_FILTER = ["institution", "is_active"]

    SEARCH_FIELDS = ["name__icontains", "email__icontains"]

    EDITFORM_CLASS = UserForm

    USE_DETAILS_TO_EDIT = False  # required to have form in NEW_TAB

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = "middle-left"
    ORQUESTRA_MENU_ORDER = 10
    ORQUESTRA_MENU_ICON = "users"

    @classmethod
    def has_permissions(cls, user):
        if user.is_superuser:
            return True
        return False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._list.headers = [
            "Name",
            "Email address",
            "Institution",
            "Active",
            "Date joined",
            "Last login",
        ]
        self._list.custom_filter_labels = {"is_active": "Active"}

    def has_add_permissions(self):
        return False

    def has_remove_permissions(self, obj):
        return False
