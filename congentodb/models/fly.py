from django.db import models

class Fly(models.Model):

    id        = models.AutoField('Id', primary_key=True)
    created   = models.DateTimeField('Created', auto_now_add=True)
    modified  = models.DateTimeField('Updated', auto_now=True)

    chrx      = models.CharField('chrX', max_length=60, blank=True, null=True)
    chry      = models.CharField('chrY', max_length=60, blank=True, null=True)
    bal1      = models.CharField('bal1', max_length=60, blank=True, null=True)
    chr2      = models.CharField('chr2', max_length=60, blank=True, null=True)
    bal2      = models.CharField('bal2', max_length=60, blank=True, null=True)
    chr3      = models.CharField('chr3', max_length=60, blank=True, null=True)
    bal3      = models.CharField('bal3', max_length=60, blank=True, null=True)
    chr4      = models.CharField('chr4', max_length=60, blank=True, null=True)
    chru      = models.CharField('chrU', max_length=60, blank=True, null=True)
    legacy1   = models.CharField('Legacy ID 1', max_length=30, blank=True, null=True)
    legacy2   = models.CharField('Legacy ID 2', max_length=30, blank=True, null=True)
    legacy3   = models.CharField('Legacy ID 3', max_length=30, blank=True, null=True)
    flydbid   = models.CharField('Fly DB ID', max_length=50, blank=True, null=True)
    hospital  = models.BooleanField('Hospital')
    died      = models.BooleanField('Died')
    genotype  = models.CharField('Genotype', max_length=255, blank=True, null=True)

    category = models.CharField('Category', max_length=255, blank=True, null=True)
    specie   = models.CharField('Specie', max_length=255,   blank=True, null=True)

    remote_id   = models.BigIntegerField('Remote id')
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id', ]
        verbose_name = "Fly stock"
        verbose_name_plural = "Flies stock"

    def __str__(self):
        return str(self.remote_id)

    @property
    def institution_name(self):
        if self.institution is None:
            return None
        else:
            return self.institution.name

    def genotype(self):

        columns = [
            self.chrx, self.chry,
            self.chr2, self.chr3, self.chr4,
            self.bal1, self.bal2, self.bal3
        ]

        if len([x is None or x.strip()=='' for x in columns])==8:
            result = '' if (self.chru is None or self.chru.strip()=='') else f"{self.chru}"
        else:
            result = self.chrx

            if self.chry.strip() != "":
                result += '/Y' + self.chry

            if self.bal1.strip() != "":
                result += '/' + self.bal1

            ##############################
            result += '; '

            if self.chr2.strip() != "":
                result += self.chr2

            if self.bal2.strip() != "":
                result += '/' + self.bal2

            ##############################
            result += '; '

            if self.chr3.strip() != "":
                result += self.chr3

            if self.bal3.strip() != "":
                result += '/' + self.bal3
            ##############################
            result += '; '

            if self.chr4.strip() != "": result += self.chr4

            if self.chru.strip() != "":
                result += ' (' + self.chru + ')'

        return result