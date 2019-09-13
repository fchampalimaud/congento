from django.db import models

from fishdb.base_fish import AbstractFish
from fishdb.models.category import AbstractCategory
from fishdb.models.species import AbstractSpecies


class CongentoRecord(models.Model):
    congento_id = models.PositiveIntegerField("Congento ID")

    class Meta:
        abstract = True


class Fish(CongentoRecord, AbstractFish):
    #redirect foreign keys to the
    category = models.ForeignKey(
        to="Category", on_delete=models.PROTECT, related_name="%(app_label)s_%(class)s_related"
    )
    species = models.ForeignKey(
        to="Species", on_delete=models.PROTECT, related_name="%(app_label)s_%(class)s_related"
    )

class Category(AbstractCategory):
    ...


class Species(AbstractSpecies):
    ...
