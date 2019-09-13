from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.management.utils import get_random_secret_key


class Institution(models.Model):
    """
    Institution part of the Congento network.
    """

    name = models.CharField(verbose_name="Name", max_length=150)
    acronym = models.CharField(verbose_name="Acronym", max_length=20, blank=True)
    key = models.CharField(
        verbose_name="Key",
        max_length=50,
        blank=True,
        default=get_random_secret_key,
        validators=[MinLengthValidator(50), MaxLengthValidator(50)],
    )

    def __str__(self):
        return self.name
