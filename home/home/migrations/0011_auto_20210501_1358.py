# Generated by Django 3.1.7 on 2021-05-01 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210501_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
