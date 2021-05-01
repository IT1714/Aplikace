# Generated by Django 3.2 on 2021-05-01 17:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20210501_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='employees',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]