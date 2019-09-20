# Generated by Django 2.1.12 on 2019-09-18 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congentodb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('availability', models.CharField(choices=[('live', 'Live'), ('cryo', 'Cryopreserved'), ('both', 'Live & Cryopreserved'), ('none', 'Unavailable')], max_length=4)),
                ('link', models.URLField(blank=True)),
                ('strain_name', models.CharField(max_length=255)),
                ('common_name', models.CharField(blank=True, max_length=50)),
                ('background', models.CharField(max_length=30)),
                ('genotype', models.CharField(max_length=30)),
                ('phenotype', models.CharField(max_length=30)),
                ('origin', models.CharField(blank=True, help_text='Leave blank for in-house generated lines', max_length=80, verbose_name='Imported from')),
                ('quarantine', models.BooleanField(default=False, verbose_name='Quarantine')),
                ('mta', models.BooleanField(default=True, verbose_name='MTA')),
                ('line_description', models.TextField(blank=True)),
                ('category_name', models.CharField(max_length=40)),
                ('species_name', models.CharField(max_length=80)),
                ('remote_id', models.BigIntegerField(verbose_name='Remote id')),
            ],
        ),
        migrations.RemoveField(
            model_name='zebrafish',
            name='institution',
        ),
        migrations.DeleteModel(
            name='Zebrafish',
        ),
    ]