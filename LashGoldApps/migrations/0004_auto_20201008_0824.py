# Generated by Django 3.1.1 on 2020-10-08 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LashGoldApps', '0003_auto_20201008_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicearea',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
