# Generated by Django 3.1.7 on 2021-04-12 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='desc',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
    ]
