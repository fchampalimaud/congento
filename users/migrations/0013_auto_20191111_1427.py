# Generated by Django 2.2.7 on 2019-11-11 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20190924_1439'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='institutionalemaildomain',
            unique_together={('domain', 'institution')},
        ),
    ]