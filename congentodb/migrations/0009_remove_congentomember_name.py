# Generated by Django 2.1.12 on 2019-09-20 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('congentodb', '0008_congentomember_institution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='congentomember',
            name='name',
        ),
    ]
