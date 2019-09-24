import logging

from allauth.account.models import EmailAddress
from django.apps import apps
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.core.exceptions import ValidationError
from django.db import models
from model_utils import Choices

from .querysets import UserQuerySet

logger = logging.getLogger(__name__)


class User(AbstractUser):

    name = models.CharField(verbose_name="Name", max_length=255)
    display_name = models.CharField(
        verbose_name="Display name", max_length=40, blank=True
    )
    institution = models.ForeignKey(
        to="Institution", on_delete=models.CASCADE, null=True, blank=True
    )

    institution_to_validate = models.CharField(
        verbose_name="Institution (needs validation)", max_length=120, blank=True,
        help_text="Affiliation declared by the user on sign up"
    )

    # notes = models.TextField(blank=True)

    objects = UserManager()

    def __str__(self):
        return f"{self.name} <{self.email}>"

    def clean(self):
        if self.institution is None:
            raise ValidationError("Assign this User to a valid Institution.")
        else:
            self.institution_to_validate = ""

    def get_display_name(self):
        if self.display_name:
            return self.display_name
        elif self.name:
            display_name = self.name
            if len(display_name) > 40:
                display_name = display_name.split()[0]
            return display_name
        else:
            return self.username


class Institution(models.Model):
    name = models.CharField(max_length=150)
    acronym = models.CharField(max_length=20, blank=True)

    is_congento_member = models.BooleanField(
        verbose_name="Congento member", default=False
    )

    def __str__(self):
        return self.acronym or self.name


class InstitutionalEmailDomain(models.Model):
    domain = models.CharField(
        verbose_name="Email domain",
        max_length=40,
        help_text="eg. research.fchampalimaud.org",
    )
    institution = models.ForeignKey(to="Institution", on_delete=models.CASCADE,
        related_name="email_domains")
