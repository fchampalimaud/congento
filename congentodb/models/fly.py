from django.db import models
from model_utils import Choices


class Fly(models.Model):

    ORIGINS = Choices(
        ("center", "Stock Center"),
        ("internal", "Internal Lab"),
        ("external", "External Lab"),
    )

    created = models.DateTimeField('Created', auto_now_add=True)
    modified = models.DateTimeField('Updated', auto_now=True)
    categories = models.TextField('Category', blank=True, null=True)
    species = models.CharField('Species', max_length=80)
    origin = models.CharField(
        max_length=8, choices=ORIGINS, default=ORIGINS.center
    )
    origin_center = models.CharField('Stock center', max_length=100, null=True, blank=True)
    genotype = models.CharField('Genotype', max_length=255, blank=True)

    chrx = models.CharField(max_length=60, verbose_name="Chromosome X", blank=True)
    chry = models.CharField(max_length=60, verbose_name="Chromosome Y", blank=True)
    chr2 = models.CharField(max_length=60, verbose_name="Chromosome 2", blank=True)
    chr3 = models.CharField(max_length=60, verbose_name="Chromosome 3", blank=True)
    chr4 = models.CharField(max_length=60, verbose_name="Chromosome 4", blank=True)
    bal1 = models.CharField(max_length=60, verbose_name="Balancer 1", blank=True)
    bal2 = models.CharField(max_length=60, verbose_name="Balancer 2", blank=True)
    bal3 = models.CharField(max_length=60, verbose_name="Balancer 3", blank=True)
    chru = models.CharField(max_length=60, verbose_name="Unknown genotype", blank=True)

    special_husbandry_conditions = models.TextField(blank=True)
    line_description = models.TextField(blank=True)

    remote_id = models.BigIntegerField("Remote ID")
    congento_member = models.ForeignKey("CongentoMember", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Fly stock"
        verbose_name_plural = "Flies stock"

    def __str__(self):
        return str(self.remote_id)

    @property
    def institution_name(self):
        if self.congento_member.institution is None:
            return None
        else:
            return self.congento_member.institution.name

    def genotype(self):

        columns = [
            self.chrx,
            self.chry,
            self.chr2,
            self.chr3,
            self.chr4,
            self.bal1,
            self.bal2,
            self.bal3,
        ]

        if len([x is None or x.strip() == "" for x in columns]) == 8:
            result = (
                "" if (self.chru is None or self.chru.strip() == "") else f"{self.chru}"
            )
        else:
            result = self.chrx

            if self.chry.strip() != "":
                result += "/Y" + self.chry

            if self.bal1.strip() != "":
                result += "/" + self.bal1

            ##############################
            result += "; "

            if self.chr2.strip() != "":
                result += self.chr2

            if self.bal2.strip() != "":
                result += "/" + self.bal2

            ##############################
            result += "; "

            if self.chr3.strip() != "":
                result += self.chr3

            if self.bal3.strip() != "":
                result += "/" + self.bal3
            ##############################
            result += "; "

            if self.chr4.strip() != "":
                result += self.chr4

            if self.chru.strip() != "":
                result += " (" + self.chru + ")"

        return result
