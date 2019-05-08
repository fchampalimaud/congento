from django.db import models

class Institution(models.Model):

    name = models.CharField('Name', max_length=255)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.name