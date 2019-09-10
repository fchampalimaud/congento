from django.db import models

from fishdb.base_fish import AbstractFish


class CongentoRecord(models.Model):
    remote_id = models.PositiveIntegerField("Remote ID")

    class Meta:
        abstract = True


class Fish(CongentoRecord, AbstractFish):
    ...
