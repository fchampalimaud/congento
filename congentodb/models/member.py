from django.db import models
from django.conf import settings


class CongentoMember(models.Model):
    """Congento members are Institutions with API access."""

    api_user = models.OneToOneField(
        verbose_name="API User",
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="congento_member",
    )
    institution = models.OneToOneField(
        to="users.Institution",
        on_delete=models.CASCADE,
        related_name="congento_member",
        limit_choices_to={"is_congento_member": True},
    )

    def __str__(self):
        return self.institution.name
