# Generated by Django 2.1.12 on 2019-09-20 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('congentodb', '0005_auto_20190920_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='institution',
            old_name='user',
            new_name='api_user',
        ),
    ]