# Generated by Django 2.2.5 on 2019-09-25 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congentodb', '0014_auto_20190924_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rodent',
            name='background',
            field=models.CharField(blank=True, default='', max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rodent',
            name='coat_color',
            field=models.CharField(blank=True, default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rodent',
            name='inducible_cassette',
            field=models.CharField(blank=True, default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rodent',
            name='reporter_gene',
            field=models.CharField(blank=True, default='', max_length=40),
            preserve_default=False,
        ),
    ]