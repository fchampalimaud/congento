from confapp import conf
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlButton
from pyforms.controls import ControlLabel
from pyforms.controls import ControlSimpleLabel
from pyforms.controls import ControlText
from pyforms.controls import ControlTextArea
from pyforms.controls import ControlTemplate
from pyforms_web.organizers import segment
from pyforms_web.organizers import no_columns
from pyforms_web.web.middleware import PyFormsMiddleware
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django.modelviewform import ModelFormWidget
from pyforms_web.widgets.django.modelviewform import ModelViewFormWidget

from congentodb.models import Fish

from .utils import ViewPermissionsMixin


class FishViewer(ModelFormWidget):
    LAYOUT_POSITION = conf.ORQUESTRA_NEW_BIGWINDOW

    FIELDSETS = [
        ("species_name", "category_name", "strain_name", "common_name"),
        ("background", "genotype", "phenotype", "origin"),
        ("availability", "link"),
        no_columns("quarantine"),
        no_columns("mta"),
        "line_description",
    ]

    @property
    def title(self):
        try:
            return "Fish"
        except AttributeError:
            pass  # apparently it defaults to App TITLE


class ControlReadOnlyField(ControlTemplate):
    def __init__(self, obj, field, *args, **kwargs):
        super().__init__(template="congento/readonly.html", *args, **kwargs)

        try:
            field_value = getattr(obj, f"get_{field.name}_display")
        except AttributeError:
            field_value = getattr(obj, field.name)
        finally:
            if isinstance(field_value, bool):
                field_value = "Yes" if field_value else "No"
            else:
                field_value = field_value or "-"

        self.value = {
            "field_name": field.verbose_name,
            "field_value": field_value,
            "is_boolean": field.get_internal_type() == "BooleanField",
        }


class NewFishViewer(BaseWidget):

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_WINDOW

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = "Details"
        self.model = kwargs.pop("model")
        self.pk = kwargs.pop("pk")

        self.model_object = self.model.objects.get(pk=self.pk)

        self._provider = ControlLabel(
            "provider", default=str(self.model_object.congento_member.institution.name)
        )
        self._request_btn = ControlButton(
            label='<i class="ui mail icon"></i>Place Request',
            helptext="Sends an email to someone responsible",
            css="fluid primary",
            field_css="four wide",
            default=self.__request_evt,
        )

        self._request_extra = ControlTextArea(
            label="Custom Message",
            rows=2,
            helptext="Write down notes or questions.",
            field_css="twelve wide",
        )

        # Override the control used for all fields
        for field in self.model._meta.fields:
            setattr(
                self,
                field.name,
                ControlReadOnlyField(obj=self.model_object, field=field),
            )

        self.formset = [
            segment(
                ("species_name", "category_name", "strain_name", "common_name"),
                ("background", "genotype", "phenotype", "origin"),
                ("quarantine", "mta", "availability", "link"),
                "line_description",
            ),
            ("_request_extra", "_request_btn"),
        ]

    def __request_evt(self, *args, **kwargs):
        print(args, kwargs)

        user = PyFormsMiddleware.user()

        print(self._request_extra.value)
        print(user)
        print(user.email)

        print(self.model_object)
        print(self.model_object.remote_id)

        # TODO set congento member responsible contact

        return


class FishApp(ViewPermissionsMixin, ModelAdminWidget):

    UID = "fish"
    MODEL = Fish

    TITLE = "Fish"

    LIST_DISPLAY = [
        "species_name",
        "category_name",
        "strain_name",
        "genotype",
        "background",
        "origin",
        "mta",
        "availability",
    ]

    LIST_FILTER = [
        "species_name",
        "category_name",
        "quarantine",
        # "location",
        "mta",
        "availability",
        "congento_member__institution",
    ]

    SEARCH_FIELDS = [
        "strain_name__icontains",
        "common_name__icontains",
        "background__icontains",
        "genotype__icontains",
        "phenotype__icontains",
        "origin__icontains",
        "line_description__icontains",
    ]

    # EDITFORM_CLASS = FishViewer
    EDITFORM_CLASS = NewFishViewer

    USE_DETAILS_TO_EDIT = False
    USE_DETAILS_TO_ADD = False

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = "top"
    ORQUESTRA_MENU_ORDER = 4
    ORQUESTRA_MENU_ICON = "large congento-fish"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
