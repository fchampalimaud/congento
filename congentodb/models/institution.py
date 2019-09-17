from django.db import models
from django.conf import settings

class Institution(models.Model):

    name = models.CharField("Name", max_length=255)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
