from django import forms
from django.utils.translation import ugettext_lazy as _

from allauth.account.forms import SignupForm

from .models import InstitutionalEmailDomain
# from .models import Institution

class SignupForm(SignupForm):
    name = forms.CharField(
        max_length=150,
        label=_("Full Name"),
        required=True,
        widget=forms.TextInput(attrs={"placeholder": _("Full Name")}),
    )

    institution_name = forms.CharField(
        max_length=150,
        label=_("Institution"),
        required=False,
        widget=forms.TextInput(attrs={"placeholder": _("Institution")}),
    )


    def custom_signup(self, request, user):

        print(self.cleaned_data)


        user.name = self.cleaned_data["name"]

        domain = self.cleaned_data["email"].split("@")[1]

        try:
            institution = InstitutionalEmailDomain.objects.get(domain=domain).institution
        except InstitutionalEmailDomain.DoesNotExist:
            user.institution_to_validate = self.cleaned_data["institution_name"]
        else:
            user.institution = institution

        user.save()

        print(user.institution)

        return user
