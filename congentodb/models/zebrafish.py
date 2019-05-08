from django.db import models
from model_utils import Choices

class Zebrafish(models.Model):

    LINES = Choices(
        ("wt", "WT"),
        ("tg", "Tg"),
        ("mu", "Mutant"),
        ("cko", "CRISPR KO"),
        ("cki", "CRISPR KI"),
        ("other", "Other"),
    )

    AVAILABILITIES = Choices(
        ("live", "Live"),
        ("cryo", "Cryopreserved"),
        ("both", "Live & Cryopreserved"),
        ("none", "Unavailable"),
    )

    created     = models.DateTimeField('Created', auto_now_add=True)
    modified    = models.DateTimeField('Updated', auto_now=True)
    background = models.CharField(max_length=20)
    genotype   = models.CharField(max_length=20)
    phenotype  = models.CharField(max_length=20)
    origin     = models.CharField(max_length=20)

    # Fields shared with other congento animal models
    availability = models.CharField(max_length=4, choices=AVAILABILITIES)
    comments     = models.TextField(blank=True)
    link         = models.URLField(blank=True)
    mta          = models.BooleanField(verbose_name="MTA", default=False)

    line_name = models.CharField(max_length=20)
    line_number = models.CharField(max_length=20)
    line_type = models.CharField(max_length=5, choices=LINES)
    line_type_other = models.CharField(max_length=20, verbose_name="", blank=True)

    remote_id = models.BigIntegerField('Remote id')
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE)


    def __str__(self):
        return self.line_name

    @property
    def institution_name(self):
        if self.institution is None:
            return None
        else:
            return self.institution.name