# Generated by Django 3.1.7 on 2021-06-08 14:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0017_auto_20210521_0005'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='register_table',
            new_name='profile',
        ),
    ]
